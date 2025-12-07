# quiz_manager.py
import random
import numpy as np

def generate_matrix_quiz():
    """Buat soal penjumlahan atau perkalian matriks"""
    A = np.random.randint(1, 5, (2, 2))
    B = np.random.randint(1, 5, (2, 2))
    ops = random.choice(['+', '*'])

    question = f"Hitung hasil dari A {ops} B\nA = {A.tolist()}\nB = {B.tolist()}"
    correct = A + B if ops == '+' else A.dot(B)
    return question, correct


def generate_spl_quiz():
    """Buat soal SPL sederhana 2x2 (Pastikan tidak singular)"""
    while True:
        A = np.random.randint(1, 5, (2, 2))
        # Cek apakah determinan tidak nol (matriks aman)
        if abs(np.linalg.det(A)) > 1e-9: 
            break
            
    B = np.random.randint(1, 10, (2,))
    x = np.linalg.solve(A, B)
    question = f"Temukan x dan y jika {A.tolist()} * [x,y]ᵀ = {B.tolist()}"
    return question, x


def generate_vector_quiz():
    """Buat soal dot product atau cross product"""
    A = np.random.randint(1, 6, (3,))
    B = np.random.randint(1, 6, (3,))
    ops = random.choice(["dot", "cross"])
    if ops == "dot":
        question = f"Hitung dot product dari A·B\nA={A.tolist()}, B={B.tolist()}"
        correct = np.dot(A, B)
    else:
        question = f"Hitung cross product dari A×B\nA={A.tolist()}, B={B.tolist()}"
        correct = np.cross(A, B)
    return question, correct
