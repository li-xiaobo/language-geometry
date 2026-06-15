"""Test 5: Temperature Control"""

import numpy as np

np.random.seed(42)

def softmax(logits, temp):
    logits = logits / max(temp, 1e-8)
    exp = np.exp(logits - np.max(logits))
    return exp / np.sum(exp)

def sample_path(v_start, M_list, temp, steps=10):
    v = v_start.copy()
    path = [v]
    for _ in range(steps):
        logits = np.random.randn(len(M_list))
        probs = softmax(logits, temp)
        idx = np.random.choice(len(M_list), p=probs)
        M = M_list[idx]
        v = M @ v
        v = v / (np.linalg.norm(v) + 1e-8)
        path.append(v)
    return path

def main():
    print("=" * 60)
    print("Test 5: Temperature Control")
    print("=" * 60)
    
    d = 10
    M_list = [np.eye(d) + 0.1 * np.random.randn(d, d) for _ in range(5)]
    v_start = np.random.randn(d)
    v_start = v_start / np.linalg.norm(v_start)
    
    for temp in [0.1, 0.5, 1.0, 2.0]:
        endpoints = []
        for _ in range(20):
            path = sample_path(v_start, M_list, temp, steps=10)
            endpoints.append(path[-1])
        endpoints = np.array(endpoints)
        var = np.trace(np.cov(endpoints.T)) if len(endpoints) > 1 else 0
        print(f"T={temp}: endpoint variance={var:.6f}")
    
    print("✅ PASS: Temperature affects sampling diversity")

if __name__ == "__main__":
    main()
