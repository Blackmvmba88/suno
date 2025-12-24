#!/usr/bin/env python3
"""
Generate an index of all metadata files for quick searching.

Usage:
    python generate_index.py --output metadata/index.json
"""

import json
import yaml
from pathlib import Path
import argparse
from typing import Dict, List, Any


def extract_key_fields(data: Dict) -> Dict[str, Any]:
    """Extract key fields from metadata for the index."""
    index_entry = {
        'track_id': data.get('track_id'),
        'title': data.get('title'),
        'artist': data.get('artist'),
    }
    
    # Musical info
    if 'musical' in data:
        musical = data['musical']
        index_entry.update({
            'genre': musical.get('genre'),
            'subgenre': musical.get('subgenre'),
            'bpm': musical.get('bpm'),
            'key': musical.get('key'),
        })
    
    # Mood
    if 'mood' in data:
        mood = data['mood']
        index_entry.update({
            'mood_primary': mood.get('primary'),
            'energy_level': mood.get('energy_level'),
        })
    
    # Tags
    if 'tags' in data:
        index_entry['tags'] = data['tags']
    
    # Creation date
    index_entry['creation_date'] = data.get('creation_date')
    
    return index_entry


def generate_index(metadata_dir: Path) -> Dict[str, Any]:
    """Generate index from all metadata files."""
    index = {
        'tracks': [],
        'genres': set(),
        'moods': set(),
        'artists': set(),
        'total_tracks': 0,
    }
    
    # Find all YAML files
    yaml_files = list(metadata_dir.glob('**/*.yaml')) + list(metadata_dir.glob('**/*.yml'))
    
    for filepath in yaml_files:
        # Skip schema file
        if 'schema' in filepath.name.lower():
            continue
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if not isinstance(data, dict):
                continue
            
            # Extract key fields
            track_entry = extract_key_fields(data)
            track_entry['file'] = str(filepath.relative_to(metadata_dir.parent))
            
            index['tracks'].append(track_entry)
            
            # Collect unique values
            if track_entry.get('genre'):
                index['genres'].add(track_entry['genre'])
            if track_entry.get('mood_primary'):
                index['moods'].add(track_entry['mood_primary'])
            if track_entry.get('artist'):
                index['artists'].add(track_entry['artist'])
            
        except Exception as e:
            print(f"Warning: Could not process {filepath}: {e}")
    
    index['total_tracks'] = len(index['tracks'])
    
    # Convert sets to sorted lists for JSON serialization
    index['genres'] = sorted(list(index['genres']))
    index['moods'] = sorted(list(index['moods']))
    index['artists'] = sorted(list(index['artists']))
    
    return index


def main():
    parser = argparse.ArgumentParser(description='Generate metadata index')
    parser.add_argument(
        '--metadata-dir',
        type=Path,
        default=Path('metadata'),
        help='Directory containing metadata files'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('metadata/index.json'),
        help='Output file for the index'
    )
    
    args = parser.parse_args()
    
    if not args.metadata_dir.exists():
        print(f"Error: Metadata directory '{args.metadata_dir}' does not exist")
        return 1
    
    print(f"Generating index from {args.metadata_dir}...")
    
    index = generate_index(args.metadata_dir)
    
    # Ensure output directory exists
    args.output.parent.mkdir(parents=True, exist_ok=True)
    
    # Write index
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Index generated: {args.output}")
    print(f"   Total tracks: {index['total_tracks']}")
    print(f"   Genres: {len(index['genres'])}")
    print(f"   Moods: {len(index['moods'])}")
    print(f"   Artists: {len(index['artists'])}")
    
    return 0


if __name__ == '__main__':
    exit(main())
