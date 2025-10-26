# spl_logic.py
import numpy as np

def read_table_to_matrix(table):
    """
    Mengonversi data dari QTableWidget ke dua matriks numpy: A (koefisien) dan B (konstanta)
    """
    rows = table.rowCount()
    cols = table.columnCount()
    A = []
    B = []

    for i in range(rows):
        row_data = []
        for j in range(cols - 1):  # semua kolom kecuali kolom terakhir (konstanta)
            item = table.item(i, j)
            value = float(item.text()) if item and item.text() != "" else 0.0
            row_data.append(value)
        A.append(row_data)

        # kolom terakhir = konstanta
        konst_item = table.item(i, cols - 1)
        konst_val = float(konst_item.text()) if konst_item and konst_item.text() != "" else 0.0
        B.append(konst_val)

    return np.array(A, dtype=float), np.array(B, dtype=float)


def solve_gaussian(A, B):
    """ Menyelesaikan SPL dengan metode eliminasi Gauss """
    try:
        n = len(B)
        augmented = np.concatenate((A, B.reshape(-1, 1)), axis=1)

        # Eliminasi maju
        for i in range(n):
            if augmented[i][i] == 0:
                for j in range(i+1, n):
                    if augmented[j][i] != 0:
                        augmented[[i, j]] = augmented[[j, i]]
                        break

            pivot = augmented[i][i]
            augmented[i] = augmented[i] / pivot

            for j in range(i + 1, n):
                factor = augmented[j][i]
                augmented[j] = augmented[j] - factor * augmented[i]

        # Substitusi balik
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = augmented[i][-1] - np.dot(augmented[i][i+1:n], x[i+1:n])

        return x
    except Exception as e:
        return f"Error (Gaussian): {e}"


def solve_inverse(A, B):
    """ Menyelesaikan SPL dengan metode matriks invers """
    try:
        invA = np.linalg.inv(A)
        x = np.dot(invA, B)
        return x
    except np.linalg.LinAlgError:
        return "Matriks tidak dapat diinvers (singular)."


def solve_cramer(A, B):
    """ Menyelesaikan SPL dengan aturan Cramer """
    try:
        detA = np.linalg.det(A)
        if detA == 0:
            return "Determinan nol, SPL tidak memiliki solusi unik."

        n = A.shape[0]
        x = np.zeros(n)

        for i in range(n):
            Ai = np.copy(A)
            Ai[:, i] = B
            x[i] = np.linalg.det(Ai) / detA
        return x
    except Exception as e:
        return f"Error (Cramer): {e}"
