# spl_logic.py
import numpy as np

def read_table_to_matrix(table):
    """Mengonversi data dari QTableWidget ke matriks A dan B"""
    rows = table.rowCount()
    cols = table.columnCount()
    A = []
    B = []

    for i in range(rows):
        row_data = []
        for j in range(cols - 1):  # kolom variabel
            item = table.item(i, j)
            val = float(item.text()) if item and item.text() else 0.0
            row_data.append(val)
        A.append(row_data)

        # kolom konstanta (terakhir)
        item_b = table.item(i, cols - 1)
        val_b = float(item_b.text()) if item_b and item_b.text() else 0.0
        B.append(val_b)

    return np.array(A, dtype=float), np.array(B, dtype=float)

def solve_gaussian(A, B):
    """Eliminasi Gauss dengan Output Step-by-Step"""
    try:
        n = len(B)
        # Gabungkan A dan B menjadi matriks augmented
        M = np.hstack((A, B.reshape(-1, 1)))
        
        steps = ["=== MATRIKS AWAL ==="]
        steps.append(str(M))
        steps.append("\n=== PROSES ELIMINASI ===")

        # Eliminasi Maju
        for i in range(n):
            # Pivot checking
            if M[i][i] == 0:
                # Cari baris di bawahnya untuk ditukar
                for k in range(i+1, n):
                    if M[k][i] != 0:
                        M[[i, k]] = M[[k, i]]
                        steps.append(f"Tukar Baris R{i+1} dengan R{k+1} (Pivot 0):")
                        steps.append(str(M))
                        break
                else:
                    return "Error: Matriks Singular (Pivot 0 tidak bisa ditukar)"

            # Buat pivot menjadi 1 (Opsional di Gauss murni, tapi bagus untuk visualisasi)
            pivot = M[i][i]
            if pivot != 1:
                M[i] = M[i] / pivot
                steps.append(f"R{i+1} dibagi {pivot:.2f} agar pivot utama = 1:")
                steps.append(str(M))

            # Nol-kan baris di bawahnya
            for j in range(i + 1, n):
                factor = M[j][i]
                if factor != 0:
                    M[j] = M[j] - factor * M[i]
                    steps.append(f"R{j+1} - ({factor:.2f} * R{i+1}):")
                    steps.append(str(M))

        # Substitusi Balik
        steps.append("\n=== SUBSTITUSI BALIK ===")
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            val = M[i][-1]
            sum_val = sum(M[i][j] * x[j] for j in range(i + 1, n))
            x[i] = val - sum_val
            steps.append(f"x{i+1} = {val:.2f} - {sum_val:.2f} = {x[i]:.4f}")

        steps.append("\n=== HASIL AKHIR ===")
        result_str = "\n".join([f"x{i+1} = {val:.4f}" for i, val in enumerate(x)])
        steps.append(result_str)

        return "\n".join(steps)

    except Exception as e:
        return f"Terjadi kesalahan: {e}"

def solve_inverse(A, B):
    try:
        invA = np.linalg.inv(A)
        x = np.dot(invA, B)
        return str(x)
    except:
        return "Matriks Singular (Tidak punya invers)"

def solve_cramer(A, B):
    try:
        n = A.shape[0]
        detA = np.linalg.det(A)
        if abs(detA) < 1e-9:
            return "Determinan 0, Metode Cramer tidak bisa dipakai."
        
        x = []
        info = [f"Det Utama = {detA:.2f}"]
        for i in range(n):
            Ai = A.copy()
            Ai[:, i] = B
            detAi = np.linalg.det(Ai)
            val = detAi / detA
            x.append(val)
            info.append(f"Dx{i+1} = {detAi:.2f} -> x{i+1} = {val:.4f}")
        
        return "\n".join(info)
    except Exception as e:
        return str(e)