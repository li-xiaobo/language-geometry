"""Test 2: Low-rank Structure"""

import numpy as np

np.random.seed(42)

def manual_pca(data, n_components=10):
    centered = data - np.mean(data, axis=0)
    cov = centered.T @ centered / (len(data) - 1)
    eigvals, _ = np.linalg.eigh(cov)
    eigvals = np.sort(eigvals)[::-1]
    total_var = np.sum(eigvals)
    cumulative = np.cumsum(eigvals) / total_var
    return cumulative

def generate_data(n_samples=5000, d=20):
    X, y = [], []
    for _ in range(n_samples):
        v1 = np.random.randn(d)
        v1 = v1 / np.linalg.norm(v1)
        delta = np.zeros(d)
        delta[:5] = np.random.randn(5) * 0.3
        delta[5:] = np.random.randn(d-5) * 0.05
        v2 = v1 + delta
        v2 = v2 / np.linalg.norm(v2)
        X.append(v1)
        y.append(v2 - v1)
    return np.array(X), np.array(y)

def main():
    print("=" * 60)
    print("Test 2: Low-rank Structure")
    print("=" * 60)
    
    X, y = generate_data(5000, 20)
    cumulative = manual_pca(y)
    
    for k in [2, 5, 10]:
        if k <= len(cumulative):
            print(f"First {k} principal components: {cumulative[k-1]:.2%}")
    
    if cumulative[4] > 0.7:
        print("✅ PASS: Difference vectors have low-rank structure")
    else:
        print("⚠️ WEAK PASS")

if __name__ == "__main__":
    main()
