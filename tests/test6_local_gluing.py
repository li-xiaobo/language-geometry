"""Test 6: Local Gluing"""

import numpy as np

np.random.seed(42)

def generate_section(length=5, d=10):
    v = np.random.randn(d)
    v = v / np.linalg.norm(v)
    seq = [v]
    for _ in range(length - 1):
        delta = np.random.randn(d) * 0.1
        v = v + delta
        v = v / np.linalg.norm(v)
        seq.append(v)
    return np.array(seq)

def compatibility(seq1, seq2, overlap_size=2):
    overlap1 = seq1[-overlap_size:]
    overlap2 = seq2[:overlap_size]
    dist = np.mean([np.linalg.norm(a - b) for a, b in zip(overlap1, overlap2)])
    return dist

def main():
    print("=" * 60)
    print("Test 6: Local Gluing")
    print("=" * 60)
    
    d = 10
    overlap = 2
    mid = np.random.randn(d)
    mid = mid / np.linalg.norm(mid)
    
    seq1 = generate_section(5, d)
    seq2 = generate_section(5, d)
    seq1[-overlap:] = mid
    seq2[:overlap] = mid
    
    dist_compat = compatibility(seq1, seq2, overlap)
    
    seq1 = generate_section(5, d)
    seq2 = generate_section(5, d)
    dist_incompat = compatibility(seq1, seq2, overlap)
    
    print(f"Compatible distance: {dist_compat:.6f}")
    print(f"Incompatible distance: {dist_incompat:.6f}")
    
    if dist_compat < dist_incompat:
        print("✅ PASS: Compatible fragments can glue")
    else:
        print("❌ FAIL")

if __name__ == "__main__":
    main()
