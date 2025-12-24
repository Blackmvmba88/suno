# Copilot / AI Agent Instructions — Sudoku Inteligente (MVP)

Purpose: short, actionable guidance so an AI coding agent can quickly be productive in this repo.

## Quick summary (big picture)
- Single FastAPI service (backend) that also serves a static web UI from `backend/app/static`.
- Two core domains:
  - Solver: logical Sudoku puzzle generation & backtracking solver (`backend/app/solver.py`).
  - OCR: image -> 9x9 board extraction using OpenCV + pytesseract, optional TFLite digit model (`backend/app/ocr.py`).
- Packaging: PyInstaller-based macOS `.app` + `.dmg` via `scripts/build_mac.sh` and `.github/workflows/macos_build.yml` (CI uses macOS runners and **Python 3.11**).

## Quick start (commands you can run locally)
- Setup env & deps (use Python 3.11 for parity with CI):
  - python3.11 -m venv .venv && source .venv/bin/activate
  - pip install -r backend/requirements.txt
- Run server (dev):
  - uvicorn backend.app.main:app --reload --port 8000
  - or: python backend/entrypoint.py (opens browser)
- Run tests (recommended):
  - PYTHONPATH=backend pytest backend/tests -q  # or: cd backend && pytest
- Package macOS locally (on macOS):
  - chmod +x scripts/build_mac.sh && ./scripts/build_mac.sh

## Useful endpoints & behavior (examples)
- GET /api/new?difficulty=easy|medium|hard|expert  -> returns { puzzle, solution }
- POST /api/solve  -> accepts { board: [[...]] } and returns { solution }
- POST /api/ocr  -> multipart file upload; returns { board, confidences } (use curl: `curl -F "file=@/path/to/img.png" http://localhost:8000/api/ocr`)
- POST /api/ocr/debug  -> returns PNG bytes with overlay for visual debugging
- GET/POST /api/ocr/config  -> read/write OCR preprocessing config (repo `config/ocr_config.yaml` by default)

## Important implementation details & repo-specific conventions (do not assume otherwise)
- Import resilience: `backend/app/main.py` uses layered try/except imports to support three contexts: repository module import (`backend.app.*`), package-like import (`app.*`), and running file directly. When editing imports, keep this pattern or add tests for new import contexts.
- Static files & packaging:
  - Static UI served under `/static` (see `_get_static_dir()` in `main.py`) to avoid shadowing API routes.
  - When packaged with PyInstaller, static files are read from `sys._MEIPASS`. `scripts/build_mac.sh` includes `--add-data backend/app/static:app/static` and `--add-data backend/app/models:app/models`.
- OCR config path: `OCR_CONFIG` is loaded from a computed path in `backend/app/ocr.py`. The code resolves to `os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'config', 'ocr_config.yaml')` which effectively points to the repo-level `config/ocr_config.yaml`. `load_config()` performs a shallow merge with `DEFAULT_CONFIG`. Be careful editing this path—tests rely on the existing behavior (GET reads defaults if missing; POST will create/overwrite the resolved file).
- TFLite optional: TFLite interpreter may not be available; code falls back to pytesseract. To enable/rehabilitate TFLite digits:
  - Train/convert using `backend/tools/train_digit_model.py --out backend/app/models/digit_model.tflite` (requires TensorFlow),
  - Toggle `tflite.enabled` in config or use `/api/ocr/config` to set it.
- System dependencies: OCR requires the Tesseract binary (not just the Python wrapper). Install with `brew install tesseract` on macOS, or system package on Linux.

## Tests & debugging tips
- Tests use FastAPI `TestClient` and exercise endpoints (`backend/tests/*`). Run `pytest backend/tests` from repo root.
- OCR debug endpoint `/api/ocr/debug` is useful for visually validating preprocessing and warp steps.
- Fonts: test image generation uses `Arial.ttf` when available, otherwise falls back to `ImageFont.load_default()` — tests are robust to missing system fonts.

## When editing: test matrix & CI considerations
- If you change packaging behavior, run `./scripts/build_mac.sh` locally (macOS) and check the artifact in `dist/`.
- CI macos workflow is `.github/workflows/macos_build.yml` — it installs system deps (brew, tesseract), sets up Python 3.11 and runs `./scripts/build_mac.sh`.
- Signing & notarization are **optional** and gated on secrets/env vars: `APPLE_API_KEY`, `APPLE_API_KEY_ID`, `APPLE_TEAM_ID`, `APPLE_SIGN_IDENTITY`. Add these to CI only if you control an Apple developer account.
- Add/adjust tests in `backend/tests/` for any behavioral changes to OCR, solver, or config persistence.

## Small implementation examples to reference
- Solver uniqueness heuristic: `backend/app/solver.py` uses `count_solutions(..., limit=2)` to ensure generated puzzles have unique solutions.
- OCR flow: `extract_board_from_bytes()` (in `ocr.py`) performs warp -> resize -> per-cell preprocess -> detect largest contour -> classify using TFLite (if available) else pytesseract.
- Frontend interaction: `backend/app/static/app.js` fetches `/api/new`, `/api/solve`, `/api/ocr` and auto-invokes solving after successful OCR.

---
If anything important is missing or a section is unclear, tell me what you'd like expanded or any specific workflow you'd like me to include (CI, release, testing edge cases), and I will iterate. ✅