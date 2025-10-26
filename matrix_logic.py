import numpy as np

class MatObj:
    # Wrapper untuk matriks/skalar agar operator + - * diarahkan ke fungsi khusus
    def __init__(self, value) :
        self.value = value

    def __init__(self, value):
        self.value = value  # bisa berupa float (skalar) atau numpy.ndarray (matriks)

    def __add__(self, other):
        return MatObj(penjumlahan(self.value, other.value))

    def __sub__(self, other):
        return MatObj(pengurangan(self.value, other.value))

    def __mul__(self, other):
        return MatObj(perkalian(self.value, other.value))

    def __repr__(self):
        return repr(self.value)
    
"""""
def input_matriks(nama):
    m = int(input(f"Masukkan jumlah baris matriks {nama}: "))
    n = int(input(f"Masukkan jumlah kolom matriks {nama}: "))
    print(f"Masukkan elemen-elemen matriks {nama}:")
    data = []
    for i in range(m):
        row = list(map(float, input(f"Baris {i+1}: ").split()))
        while len(row) != n:
            print("Jumlah elemen tidak sesuai, coba lagi.")
            row = list(map(float, input(f"Baris {i+1}: ").split()))
        data.append(row)
    return MatObj(np.array(data))

def input_skalar(nama):
    return MatObj(float(input(f"Masukkan nilai skalar {nama}: ")))
"""""

def penjumlahan(x, y):
    return x + y

def pengurangan(x, y):
    return x - y

def perkalian(x, y):
    if np.isscalar(x) and isinstance(y, np.ndarray):
        return x * y
    if np.isscalar(y) and isinstance(x, np.ndarray):
        return x*y
    if isinstance(x, np.ndarray) and isinstance(y, np.ndarray):
        # validasi dimensi: (m x n) * (n x p)
        if x.shape[1] != y.shape[0]:
            raise ValueError(f"Ordo tidak sesuai untuk perkalian matriks: {x.shape} * {y.shape}")
        return x.dot(y)
    if np.isscalar(x) and np.isscalar(y):
        return x * y


# helper
def format_matobj(obj):
    if isinstance(obj, MatObj):
        v = obj.value
    else:
        v = obj
    if isinstance(v, np.ndarray):
        rows = [" ".join(map(str, row)) for row in v.tolist()]
        return "\n".join(rows)
    else:
        return str(v)