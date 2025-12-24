#!/usr/bin/env python3
"""
Validate metadata YAML files against the schema.

Usage:
    python validate_metadata.py metadata/tracks/my-track.yaml
    python validate_metadata.py metadata/tracks/  # validate all in directory
"""

import sys
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional


# Required fields
REQUIRED_FIELDS = {
    'track_id': str,
    'title': str,
    'creation_date': str,
    'musical': {
        'genre': str,
        'bpm': int,
    }
}

# Optional but recommended fields
RECOMMENDED_FIELDS = [
    'musical.key',
    'musical.time_signature',
    'mood.primary',
    'mood.energy_level',
    'tags',
]


def validate_field_type(value: Any, expected_type: type) -> bool:
    """Check if value matches expected type."""
    if expected_type == int:
        return isinstance(value, int)
    elif expected_type == str:
        return isinstance(value, str)
    elif expected_type == bool:
        return isinstance(value, bool)
    elif expected_type == list:
        return isinstance(value, list)
    elif expected_type == dict:
        return isinstance(value, dict)
    return True


def get_nested_value(data: Dict, path: str) -> Optional[Any]:
    """Get nested dictionary value using dot notation."""
    keys = path.split('.')
    value = data
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return None
    return value


def validate_required_fields(data: Dict, schema: Dict, prefix: str = '') -> List[str]:
    """Validate that all required fields are present and correct type."""
    errors = []
    
    for field, field_type in schema.items():
        full_path = f"{prefix}.{field}" if prefix else field
        
        if isinstance(field_type, dict):
            # Nested structure
            if field not in data:
                errors.append(f"Missing required field: {full_path}")
            elif not isinstance(data[field], dict):
                errors.append(f"Field {full_path} must be a dictionary")
            else:
                # Recursively validate nested fields
                errors.extend(validate_required_fields(
                    data[field], field_type, full_path
                ))
        else:
            # Simple field
            if field not in data:
                errors.append(f"Missing required field: {full_path}")
            elif not validate_field_type(data[field], field_type):
                errors.append(
                    f"Field {full_path} has incorrect type. "
                    f"Expected {field_type.__name__}, got {type(data[field]).__name__}"
                )
    
    return errors


def check_recommended_fields(data: Dict) -> List[str]:
    """Check for recommended but optional fields."""
    warnings = []
    
    for field_path in RECOMMENDED_FIELDS:
        value = get_nested_value(data, field_path)
        if value is None:
            warnings.append(f"Recommended field missing: {field_path}")
    
    return warnings


def validate_bpm(bpm: int) -> Optional[str]:
    """Validate BPM is in reasonable range."""
    if not (20 <= bpm <= 300):
        return f"BPM {bpm} is outside typical range (20-300)"
    return None


def validate_ratings(data: Dict) -> List[str]:
    """Validate rating fields are in 1-10 range."""
    errors = []
    
    if 'mood' in data:
        for field in ['energy_level', 'danceability', 'emotional_valence']:
            if field in data['mood']:
                value = data['mood'][field]
                if not isinstance(value, int) or not (1 <= value <= 10):
                    errors.append(f"mood.{field} must be an integer between 1 and 10")
    
    return errors


def validate_metadata_file(filepath: Path) -> tuple[bool, List[str], List[str]]:
    """
    Validate a metadata YAML file.
    
    Returns:
        (is_valid, errors, warnings)
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return False, [f"YAML parsing error: {e}"], []
    except Exception as e:
        return False, [f"Error reading file: {e}"], []
    
    if not isinstance(data, dict):
        return False, ["Root element must be a dictionary"], []
    
    errors = []
    warnings = []
    
    # Check required fields
    errors.extend(validate_required_fields(data, REQUIRED_FIELDS))
    
    # Check recommended fields
    warnings.extend(check_recommended_fields(data))
    
    # Validate specific fields
    if 'musical' in data and 'bpm' in data['musical']:
        bpm_error = validate_bpm(data['musical']['bpm'])
        if bpm_error:
            warnings.append(bpm_error)
    
    # Validate rating fields
    errors.extend(validate_ratings(data))
    
    is_valid = len(errors) == 0
    return is_valid, errors, warnings


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_metadata.py <file_or_directory>")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    
    if not path.exists():
        print(f"Error: Path '{path}' does not exist")
        sys.exit(1)
    
    # Collect files to validate
    if path.is_file():
        files = [path]
    else:
        files = list(path.glob('**/*.yaml')) + list(path.glob('**/*.yml'))
        # Exclude schema files (they're documentation, not metadata)
        files = [f for f in files if 'schema' not in f.name.lower()]
    
    if not files:
        print(f"No YAML files found in '{path}'")
        sys.exit(1)
    
    print(f"Validating {len(files)} file(s)...\n")
    
    total_valid = 0
    total_invalid = 0
    
    for filepath in files:
        is_valid, errors, warnings = validate_metadata_file(filepath)
        
        if is_valid:
            total_valid += 1
            print(f"✅ {filepath.name}: VALID")
            if warnings:
                for warning in warnings:
                    print(f"   ⚠️  {warning}")
        else:
            total_invalid += 1
            print(f"❌ {filepath.name}: INVALID")
            for error in errors:
                print(f"   ❌ {error}")
            if warnings:
                for warning in warnings:
                    print(f"   ⚠️  {warning}")
        print()
    
    # Summary
    print("=" * 60)
    print(f"Total: {len(files)} files")
    print(f"Valid: {total_valid}")
    print(f"Invalid: {total_invalid}")
    
    sys.exit(0 if total_invalid == 0 else 1)


if __name__ == '__main__':
    main()
