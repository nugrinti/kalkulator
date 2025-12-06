# io_utils.py
import json
import numpy as np

def export_to_file(filename, data):
    """
    Simpan data ke file. 
    - Jika 'data' adalah string, simpan sebagai file TXT biasa.
    - Jika 'data' adalah list/dict/numpy, simpan sebagai format JSON/String representasi.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            if isinstance(data, str):
                # Jika data hanya teks biasa (misal hasil output), tulis langsung
                f.write(data)
            elif isinstance(data, np.ndarray):
                # Jika numpy array, simpan sebagai list agar bisa dibaca manusia
                f.write(str(data.tolist()))
            else:
                # Jika dict/list objek lain, gunakan JSON agar terstruktur
                # atau gunakan str(data) jika ingin bentuk string Python
                f.write(str(data)) 
                
        return f"Data berhasil diekspor ke {filename}"
    except Exception as e:
        return f"Gagal menyimpan data: {e}"


def import_from_file(filename):
    """
    Baca data dari file.
    Mencoba membaca sebagai teks biasa.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            return content
    except Exception as e:
        return f"Gagal membaca file: {e}"