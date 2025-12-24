#!/usr/bin/env python3
"""
Search through metadata files.

Usage:
    python search_metadata.py --genre synthwave
    python search_metadata.py --bpm 110-120
    python search_metadata.py --mood nostalgic
    python search_metadata.py --artist "Suno Lab"
"""

import yaml
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional


def load_metadata_files(metadata_dir: Path) -> List[Dict[str, Any]]:
    """Load all metadata files from directory."""
    tracks = []
    
    yaml_files = list(metadata_dir.glob('**/*.yaml')) + list(metadata_dir.glob('**/*.yml'))
    
    for filepath in yaml_files:
        if 'schema' in filepath.name.lower():
            continue
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if isinstance(data, dict):
                data['_filepath'] = filepath
                tracks.append(data)
        except Exception as e:
            print(f"Warning: Could not load {filepath}: {e}")
    
    return tracks


def match_bpm_range(track: Dict, bpm_range: str) -> bool:
    """Check if track BPM is in range."""
    if 'musical' not in track or 'bpm' not in track['musical']:
        return False
    
    bpm = track['musical']['bpm']
    
    if '-' in bpm_range:
        min_bpm, max_bpm = map(int, bpm_range.split('-'))
        return min_bpm <= bpm <= max_bpm
    else:
        target_bpm = int(bpm_range)
        return abs(bpm - target_bpm) <= 5  # ±5 BPM tolerance


def match_genre(track: Dict, genre: str) -> bool:
    """Check if track matches genre."""
    if 'musical' not in track:
        return False
    
    genre_lower = genre.lower()
    track_genre = track['musical'].get('genre', '').lower()
    track_subgenre = track['musical'].get('subgenre', '').lower()
    
    return genre_lower in track_genre or genre_lower in track_subgenre


def match_mood(track: Dict, mood: str) -> bool:
    """Check if track matches mood."""
    if 'mood' not in track:
        return False
    
    mood_lower = mood.lower()
    primary = track['mood'].get('primary', '').lower()
    secondary = track['mood'].get('secondary', '').lower()
    
    return mood_lower in primary or mood_lower in secondary


def match_artist(track: Dict, artist: str) -> bool:
    """Check if track matches artist."""
    track_artist = track.get('artist', '').lower()
    return artist.lower() in track_artist


def match_tags(track: Dict, tag: str) -> bool:
    """Check if track has tag."""
    if 'tags' not in track:
        return False
    
    tag_lower = tag.lower()
    return any(tag_lower in t.lower() for t in track['tags'])


def format_track_result(track: Dict) -> str:
    """Format track for display."""
    title = track.get('title', 'Untitled')
    artist = track.get('artist', 'Unknown')
    
    details = []
    
    if 'musical' in track:
        genre = track['musical'].get('genre')
        bpm = track['musical'].get('bpm')
        key = track['musical'].get('key')
        
        if genre:
            details.append(f"Genre: {genre}")
        if bpm:
            details.append(f"BPM: {bpm}")
        if key:
            details.append(f"Key: {key}")
    
    if 'mood' in track:
        mood = track['mood'].get('primary')
        if mood:
            details.append(f"Mood: {mood}")
    
    filepath = track.get('_filepath', '')
    
    result = f"🎵 {title} - {artist}"
    if details:
        result += f"\n   {' | '.join(details)}"
    if filepath:
        result += f"\n   📁 {filepath}"
    
    return result


def main():
    parser = argparse.ArgumentParser(description='Search metadata')
    parser.add_argument('--metadata-dir', type=Path, default=Path('metadata'),
                        help='Directory containing metadata files')
    parser.add_argument('--genre', help='Filter by genre')
    parser.add_argument('--bpm', help='Filter by BPM (single value or range like 110-120)')
    parser.add_argument('--mood', help='Filter by mood')
    parser.add_argument('--artist', help='Filter by artist')
    parser.add_argument('--tag', help='Filter by tag')
    parser.add_argument('--limit', type=int, help='Limit number of results')
    
    args = parser.parse_args()
    
    if not args.metadata_dir.exists():
        print(f"Error: Directory '{args.metadata_dir}' does not exist")
        return 1
    
    # Load all tracks
    tracks = load_metadata_files(args.metadata_dir)
    
    if not tracks:
        print("No metadata files found")
        return 1
    
    print(f"Loaded {len(tracks)} tracks")
    
    # Apply filters
    results = tracks
    
    if args.genre:
        results = [t for t in results if match_genre(t, args.genre)]
        print(f"After genre filter: {len(results)} tracks")
    
    if args.bpm:
        results = [t for t in results if match_bpm_range(t, args.bpm)]
        print(f"After BPM filter: {len(results)} tracks")
    
    if args.mood:
        results = [t for t in results if match_mood(t, args.mood)]
        print(f"After mood filter: {len(results)} tracks")
    
    if args.artist:
        results = [t for t in results if match_artist(t, args.artist)]
        print(f"After artist filter: {len(results)} tracks")
    
    if args.tag:
        results = [t for t in results if match_tags(t, args.tag)]
        print(f"After tag filter: {len(results)} tracks")
    
    # Apply limit
    if args.limit:
        results = results[:args.limit]
    
    # Display results
    print(f"\n{'=' * 60}")
    print(f"Found {len(results)} matching track(s):\n")
    
    for track in results:
        print(format_track_result(track))
        print()
    
    return 0


if __name__ == '__main__':
    exit(main())
