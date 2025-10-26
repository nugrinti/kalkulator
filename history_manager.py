# history_manager.py
import json
import datetime
import os

HISTORY_FILE = "history.json"

def load_history():
    """Baca seluruh history dari file JSON"""
    if not os.path.exists(HISTORY_FILE):
        return {"matrix": [], "spl": [], "vector": []}

    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_history(data):
    """Tulis ulang history ke file JSON"""
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def add_history(mode, expression, result):
    """
    mode: 'matrix' | 'spl' | 'vector'
    expression: teks operasi
    result: hasil string
    """
    history = load_history()
    record = {
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "expression": expression,
        "result": str(result)
    }
    history[mode].append(record)
    save_history(history)


def clear_history(mode=None):
    """Hapus history tertentu atau semua"""
    history = {"matrix": [], "spl": [], "vector": []}
    if mode:
        all_history = load_history()
        all_history[mode] = []
        save_history(all_history)
    else:
        save_history(history)
