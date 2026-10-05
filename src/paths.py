"""Shared paths, independent of the current working directory."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data' / 'raw'
PROCESSED = ROOT / 'data' / 'processed'
RESULTS = ROOT / 'results'
for directory in (PROCESSED, RESULTS / 'figures', RESULTS / 'maps', RESULTS / 'tables'):
    directory.mkdir(parents=True, exist_ok=True)

def data_path(name):
    processed = PROCESSED / name
    return processed if processed.exists() or not (RAW / name).exists() else RAW / name

def result_path(name):
    suffix = Path(name).suffix.lower()
    folder = 'figures' if suffix == '.png' else 'maps' if suffix == '.html' else 'tables'
    return RESULTS / folder / name
