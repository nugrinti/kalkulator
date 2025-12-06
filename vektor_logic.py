import numpy as np
import math

def parse_vector(input_str):
    # Membersihkan input seperti "(2, -1, 3)" menjadi array
    cleaned = input_str.replace("(", "").replace(")", "").replace(",", " ").split()
    return np.array([float(x) for x in cleaned], dtype=float)

# --- TAMBAHAN UNTUK SOAL 4 (a) ---
def vector_add(vecA, vecB):
    try:
        return parse_vector(vecA) + parse_vector(vecB)
    except Exception as e: return f"Error: {e}"

def vector_sub(vecA, vecB):
    try:
        return parse_vector(vecA) - parse_vector(vecB)
    except Exception as e: return f"Error: {e}"

def vector_scale(vec, scalar):
    try:
        return parse_vector(vec) * float(scalar)
    except Exception as e: return f"Error: {e}"

# --- YANG SUDAH ADA ---
def dot_product(vecA, vecB):
    try:
        return np.dot(parse_vector(vecA), parse_vector(vecB))
    except Exception as e: return f"Error: {e}"

def cross_product(vecA, vecB):
    try:
        return np.cross(parse_vector(vecA), parse_vector(vecB))
    except Exception as e: return f"Error: {e}"

# --- TAMBAHAN UNTUK SOAL 4 (d) & (e) ---
def vector_norm(vec):
    try:
        return np.linalg.norm(parse_vector(vec))
    except Exception as e: return f"Error: {e}"

def vector_projection(vecU, vecV):
    """Proyeksi u ke arah v: (u . v / |v|^2) * v"""
    try:
        u = parse_vector(vecU)
        v = parse_vector(vecV)
        if np.linalg.norm(v) == 0: return "Vektor V adalah nol"
        scalar_proj = np.dot(u, v) / np.dot(v, v)
        return scalar_proj * v
    except Exception as e: return f"Error: {e}"

def angle_between(vecA, vecB):
    # (Kode lama Anda sudah oke, pertahankan)
    try:
        A = parse_vector(vecA)
        B = parse_vector(vecB)
        dot = np.dot(A, B)
        magA = np.linalg.norm(A)
        magB = np.linalg.norm(B)
        if magA == 0 or magB == 0: return "Vektor nol."
        cos_theta = np.clip(dot / (magA * magB), -1.0, 1.0)
        return f"{math.degrees(math.acos(cos_theta)):.2f}°"
    except Exception as e: return f"Error: {e}"