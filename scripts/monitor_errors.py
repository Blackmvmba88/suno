#!/usr/bin/env python3
"""
Lightweight error monitor for SudokuInteligente.
- Polls /api/health
- Posts a synthetic test image to /api/ocr and checks for errors
- On failure logs to STDERR and optionally sends JSON payload to ERROR_MONITOR_WEBHOOK

Usage:
  ERROR_MONITOR_WEBHOOK=https://hooks.example.com/endpoint python scripts/monitor_errors.py

Environment variables:
  HEALTH_URL (default: http://127.0.0.1:8000/api/health)
  OCR_URL (default: http://127.0.0.1:8000/api/ocr)
  INTERVAL (seconds between checks, default 60)
  ERROR_MONITOR_WEBHOOK (optional): an HTTP endpoint to POST failure JSON

This script is intentionally minimal - use a proper monitoring system for production (Prometheus, Sentry, etc.).
"""

import io
import json
import os
import sys
import time
from typing import Optional

try:
    import requests
except Exception:
    print("Missing dependency: requests. Install with `pip install requests`.", file=sys.stderr)
    raise

from PIL import Image, ImageDraw, ImageFont

HEALTH_URL = os.environ.get('HEALTH_URL', 'http://127.0.0.1:8000/api/health')
OCR_URL = os.environ.get('OCR_URL', 'http://127.0.0.1:8000/api/ocr')
INTERVAL = int(os.environ.get('INTERVAL', '60'))
WEBHOOK = os.environ.get('ERROR_MONITOR_WEBHOOK')
TIMEOUT = int(os.environ.get('REQUEST_TIMEOUT', '5'))


def make_test_image_bytes():
    W = H = 450
    img = Image.new('L', (W, H), color=255)
    d = ImageDraw.Draw(img)
    # draw grid
    for i in range(10):
        y = int(i * H / 9)
        x = int(i * W / 9)
        d.line([(0, y), (W, y)], fill=0, width=2 if i % 3 == 0 else 1)
        d.line([(x, 0), (x, H)], fill=0, width=2 if i % 3 == 0 else 1)
    # draw a couple of digits
    try:
        font = ImageFont.truetype('Arial.ttf', 60)
    except Exception:
        font = ImageFont.load_default()
    d.text((10, 10), '5', fill=0, font=font)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return buf


def post_webhook(payload: dict):
    if not WEBHOOK:
        return
    try:
        requests.post(WEBHOOK, json=payload, timeout=TIMEOUT)
    except Exception as e:
        print(f"Failed to post webhook: {e}", file=sys.stderr)


def check_health() -> Optional[str]:
    try:
        r = requests.get(HEALTH_URL, timeout=TIMEOUT)
        if r.status_code != 200:
            return f"health status {r.status_code}: {r.text}"
        j = r.json()
        if j.get('status') != 'ok':
            return f"health payload unexpected: {j}"
        return None
    except Exception as e:
        return str(e)


def check_ocr() -> Optional[str]:
    try:
        files = {'file': ('test.png', make_test_image_bytes(), 'image/png')}
        r = requests.post(OCR_URL, files=files, timeout=TIMEOUT)
        if r.status_code != 200:
            return f"ocr status {r.status_code}: {r.text}"
        j = r.json()
        if 'error' in j:
            return f"ocr returned error: {j['error']}"
        return None
    except Exception as e:
        return str(e)


def main():
    print(f"Starting monitor: health={HEALTH_URL} ocr={OCR_URL} interval={INTERVAL}s webhook={'set' if WEBHOOK else 'none'}")
    while True:
        issues = []
        h = check_health()
        if h:
            issues.append({'kind': 'health', 'detail': h})
        o = check_ocr()
        if o:
            issues.append({'kind': 'ocr', 'detail': o})
        if issues:
            payload = {'service': 'sudoku_inteligente', 'issues': issues, 'timestamp': int(time.time())}
            print(json.dumps(payload), file=sys.stderr)
            post_webhook(payload)
        time.sleep(INTERVAL)


if __name__ == '__main__':
    main()
