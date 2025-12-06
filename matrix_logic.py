import numpy as np

class MatObj:
    def __init__(self, value):
        self.value = np.array(value) if not np.isscalar(value) else value

    def __add__(self, other):
        return MatObj(penjumlahan(self.value, other.value))

    def __sub__(self, other):
        return MatObj(pengurangan(self.value, other.value))

    def __mul__(self, other):
        return MatObj(perkalian(self.value, other.value))
    
    # --- TAMBAHAN UNTUK SOAL 1 (e) ---
    def transpose(self):
        if np.isscalar(self.value): return self
        return MatObj(self.value.T)

    def inverse(self):
        if np.isscalar(self.value): return MatObj(1/self.value)
        try:
            return MatObj(np.linalg.inv(self.value))
        except np.linalg.LinAlgError:
            return "Matriks Singular (Tidak punya invers)"

    def determinant(self):
        if np.isscalar(self.value): return self.value
        if self.value.shape[0] != self.value.shape[1]: return "Bukan matriks persegi"
        return np.linalg.det(self.value)

    
    def check_type(self):
        if np.isscalar(self.value): return "Skalar"
        v = self.value
        rows, cols = v.shape
        types = []
        
        if rows == cols:
            types.append("Persegi")
            if np.allclose(v, np.eye(rows)): types.append("Identitas")
            if np.allclose(v, np.diag(np.diag(v))): types.append("Diagonal")
            if np.allclose(v, v.T): types.append("Simetris")
            # --- TAMBAHAN LOGIKA BARU ---
            if np.allclose(v, np.tril(v)): types.append("Segitiga Bawah")
            if np.allclose(v, np.triu(v)): types.append("Segitiga Atas")
        
        if np.all(v == 0): types.append("Matriks Nol")
        
        # Cek Sparse (Jika elemen bukan nol kurang dari 50%)
        if v.size > 0 and np.count_nonzero(v) / v.size < 0.5:
             types.append("Sparse")
        
        return ", ".join(types) if types else "Matriks Umum"

    def __repr__(self):
        return format_matobj(self.value)

# Fungsi helper yang sudah ada tetap sama, pastikan import numpy ada
def penjumlahan(x, y): return x + y
def pengurangan(x, y): return x - y
def perkalian(x, y):
    if np.isscalar(x) or np.isscalar(y): return x * y
    return x.dot(y)

def format_matobj(v):
    if isinstance(v, np.ndarray):
        # Format rapi untuk output
        return str(v) 
    return str(v)