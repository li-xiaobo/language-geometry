"""Test 7: Holonomy Accumulation"""

import numpy as np

np.random.seed(42)

def main():
    print("=" * 60)
    print("Test 7: Holonomy Accumulation")
    print("=" * 60)
    
    d = 5
    M_list = [np.eye(d) + 0.1 * np.random.randn(d, d) for _ in range(4)]
    M_cum = M_list[3] @ M_list[2] @ M_list[1] @ M_list[0]
    
    v_start = np.random.randn(d)
    v_start = v_start / np.linalg.norm(v_start)
    
    v_seq = v_start.copy()
    for M in M_list:
        v_seq = M @ v_seq
    v_seq = v_seq / np.linalg.norm(v_seq)
    
    v_direct = M_cum @ v_start
    v_direct = v_direct / np.linalg.norm(v_direct)
    
    diff = np.linalg.norm(v_seq - v_direct)
    print(f"Difference between sequential and direct: {diff:.10f}")
    
    if diff < 1e-6:
        print("✅ PASS: Holonomy accumulates precisely")
    else:
        print("❌ FAIL")

if __name__ == "__main__":
    main()
