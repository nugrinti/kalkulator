# vektor_logic.py
import numpy as np
import math

def parse_vector(input_str):
    """
    Mengubah input teks (misalnya "1 2 3" atau "1,2,3") menjadi numpy array
    """
    cleaned = input_str.replace(",", " ").split()
    return np.array([float(x) for x in cleaned], dtype=float)


def dot_product(vecA, vecB):
    try:
        A = parse_vector(vecA)
        B = parse_vector(vecB)
        if A.shape != B.shape:
            return "Vektor harus memiliki dimensi yang sama."
        return np.dot(A, B)
    except Exception as e:
        return f"Error (Dot Product): {e}"


def cross_product(vecA, vecB):
    try:
        A = parse_vector(vecA)
        B = parse_vector(vecB)
        if len(A) != 3 or len(B) != 3:
            return "Cross product hanya untuk vektor 3 dimensi."
        return np.cross(A, B)
    except Exception as e:
        return f"Error (Cross Product): {e}"

def angle_between(vecA, vecB):
    try:
        A = parse_vector(vecA)
        B = parse_vector(vecB)
        if A.shape != B.shape:
            return "Vektor harus memiliki dimensi yang sama."

        dot = np.dot(A, B)
        magA = np.linalg.norm(A)
        magB = np.linalg.norm(B)

        if magA == 0 or magB == 0:
            return "Vektor nol tidak memiliki arah (sudut tidak terdefinisi)."

        cos_theta = dot / (magA * magB)
        cos_theta = np.clip(cos_theta, -1.0, 1.0)  # Hindari nilai >1 atau < -1
        theta_rad = math.acos(cos_theta)
        theta_deg = math.degrees(theta_rad)

        return f"{theta_deg:.2f}°"
    except Exception as e:
        return f"Error (Angle): {e}"
