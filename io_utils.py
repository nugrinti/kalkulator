# io_utils.py
import json
import numpy as np

def export_to_file(filename, data):
    """Simpan data (numpy array, list, atau dict) ke file JSON"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            if isinstance(data, np.ndarray):
                json.dump(data.tolist(), f, indent=2)
            else:
                json.dump(data, f, indent=2)
        return f"Data berhasil diekspor ke {filename}"
    except Exception as e:
        return f"Gagal menyimpan data: {e}"


def import_from_file(filename):
    """Baca data dari file JSON dan ubah ke bentuk list"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return np.array(data)
    except Exception as e:
        return f"Gagal membaca file: {e}"
