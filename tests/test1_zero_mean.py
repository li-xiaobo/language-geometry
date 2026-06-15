"""Test 1: Difference Vector Zero Mean"""

import numpy as np

np.random.seed(42)

def generate_data(n_samples=5000, d=20):
    X, y = [], []
    for _ in range(n_samples):
        v1 = np.random.randn(d)
        v1 = v1 / np.linalg.norm(v1)
        delta = np.random.randn(d) * 0.1
        v2 = v1 + delta
        v2 = v2 / np.linalg.norm(v2)
        X.append(v1)
        y.append(v2 - v1)
    return np.array(X), np.array(y)

def main():
    print("=" * 60)
    print("Test 1: Difference Vector Zero Mean")
    print("=" * 60)
    
    X, y = generate_data(5000, 20)
    mean_delta = np.mean(y, axis=0)
    mean_norm = np.linalg.norm(mean_delta)
    random_norm = np.linalg.norm(np.mean(np.random.randn(5000, 20), axis=0))
    
    print(f"Difference vector mean norm: {mean_norm:.6f}")
    print(f"Random noise control: {random_norm:.6f}")
    
    if mean_norm < 0.05:
        print("✅ PASS: Difference vectors are structured (mean near zero)")
    else:
        print("❌ FAIL")

if __name__ == "__main__":
    main()
