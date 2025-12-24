# Copilot / AI Agent Instructions — Suno Experiments & Music AI Lab

Purpose: Guide AI agents to understand and contribute effectively to this music experimentation repository.

## 🎯 Quick summary (big picture)

This is a **creative laboratory** for music AI experimentation, not a production application:
- **Prompts**: Curated musical prompts for AI generation (`prompts/`)
- **Lyrics**: Song lyrics (AI-generated, hybrid, or human) (`lyrics/`)
- **Metadata**: Structured information about tracks - BPM, key, mood, tags (`metadata/`)
- **Experiments**: Sandbox for testing ideas and documenting learnings (`experiments/`)
- **Tools**: Python utilities for validation, search, and indexing (`tools/`)

The repository is organized for **experimentation, documentation, and learning** rather than deployment.

## 🚀 Quick start (commands you can run)

```bash
# Setup environment (Python 3.9+)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Validate metadata files
python tools/validate_metadata.py metadata/tracks/

# Generate searchable index
python tools/generate_index.py --output metadata/index.json

# Search tracks
python tools/search_metadata.py --genre synthwave
python tools/search_metadata.py --bpm 110-120
python tools/search_metadata.py --mood nostalgic
```

## 📁 Directory structure & conventions

```
/
├── prompts/           # Musical prompts for AI generation
│   ├── templates/     # Reusable prompt templates
│   └── README.md      # Prompt creation guide
├── lyrics/            # Song lyrics (various sources)
│   └── README.md      # Lyrics formatting guide
├── metadata/          # Structured track information
│   ├── schema.yaml    # Metadata schema definition
│   ├── tracks/        # Individual track metadata files
│   └── README.md      # Metadata documentation
├── experiments/       # Experimental work & documentation
│   ├── templates/     # Experiment documentation template
│   └── README.md      # Experimentation guide
├── tools/             # Python utilities
│   ├── validate_metadata.py    # Validate YAML against schema
│   ├── generate_index.py       # Create searchable index
│   └── search_metadata.py      # Search tracks by criteria
├── .gitignore         # Excludes audio files, API keys, etc.
├── .editorconfig      # Code style consistency
├── requirements.txt   # Python dependencies (currently: pyyaml)
├── CONTRIBUTING.md    # Contribution guidelines
└── README.md          # Project overview
```

## 🎵 Key workflows

### Adding a new prompt
1. Copy template: `cp prompts/templates/prompt-template.yaml prompts/my-prompt.yaml`
2. Fill in details: genre, mood, BPM, instrumentation
3. Document what works and what doesn't
4. Include usage notes and variations

### Adding track metadata
1. Copy example: `cp metadata/tracks/example-track.yaml metadata/tracks/my-track.yaml`
2. Complete all required fields (track_id, title, genre, bpm, creation_date)
3. Add optional but recommended fields (mood, tags, instruments)
4. Validate: `python tools/validate_metadata.py metadata/tracks/my-track.yaml`
5. Commit only after validation passes

### Documenting an experiment
1. Create directory: `mkdir experiments/my-experiment`
2. Copy template: `cp experiments/templates/experiment-template.md experiments/my-experiment/README.md`
3. Document: hypothesis, method, results, learnings
4. Include file references and next steps

## 📋 Metadata schema (required fields)

```yaml
track_id: string       # Unique identifier
title: string          # Track title
creation_date: string  # YYYY-MM-DD
musical:
  genre: string        # Primary genre
  bpm: integer         # Beats per minute
```

See `metadata/schema.yaml` for complete schema with optional fields.

## 🔧 Tools usage

### validate_metadata.py
Validates YAML files against schema:
- Checks required fields
- Validates types
- Warns about missing recommended fields
- Validates ranges (BPM 20-300, ratings 1-10)

### generate_index.py
Creates JSON index for fast searching:
- Extracts key fields from all tracks
- Aggregates genres, moods, artists
- Outputs to `metadata/index.json`

### search_metadata.py
Search tracks by criteria:
- `--genre`: Filter by genre (partial match)
- `--bpm`: Filter by BPM (single value ±5 or range)
- `--mood`: Filter by mood (partial match)
- `--artist`: Filter by artist name
- `--tag`: Filter by tags
- `--limit`: Limit results

## 🎨 File naming conventions

- Use **kebab-case**: `my-file-name.yaml`
- Be descriptive but concise
- Include date if relevant: `2024-12-experiment.md`
- Audio files go in `.gitignore` (too large for git)

## ⚠️ Important: What NOT to commit

- Audio files (`.mp3`, `.wav`, `.flac`, etc.) — use `.gitignore`
- API keys or secrets (`.env`, `secrets.yaml`)
- Large model files (`.h5`, `.pt`, `.pth`)
- Build artifacts or temporary files

## 🧪 Philosophy & approach

This is a **learning laboratory**, not a production system:
- **Experimentation** over perfection
- **Documentation** over code
- **Iteration** over planning
- **Learning from failures** as much as successes

When contributing:
- Document experiments even if they "fail"
- Extract actionable learnings
- Keep metadata consistent and validated
- Be creative but organized

## 📊 Quality standards

Before committing:
- [ ] Metadata validates with `validate_metadata.py`
- [ ] Required fields are complete
- [ ] File names follow conventions
- [ ] Experiments document hypothesis, method, and learnings
- [ ] No large binary files (audio, models)
- [ ] No secrets or API keys

## 🤝 Contributing

See `CONTRIBUTING.md` for detailed contribution guidelines.

Quick checklist:
- Use appropriate directory for content type
- Follow naming conventions
- Validate metadata before commit
- Document experiments thoroughly
- Keep commits focused and descriptive

## 💡 Common tasks for AI agents

When asked to optimize or improve:
- Add missing documentation
- Create workflow automation
- Improve tooling (validation, search, analysis)
- Add templates for common patterns
- Enhance metadata schema
- Create visualization tools
- Add export/import utilities

---

**Remember**: This is a creative space. The goal is learning and experimentation,
not building a perfect system. Document everything, fail fast, and iterate. 🎵✨