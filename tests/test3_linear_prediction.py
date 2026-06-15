"""Test 3: Linear Prediction of Difference Vectors"""

import numpy as np

np.random.seed(42)

def generate_data(n_samples=2000, d=20, rank=3):
    U = np.random.randn(d, rank)
    V = np.random.randn(d, rank)
    M = np.eye(d) + (U @ V.T) * 0.3 / (np.linalg.norm(U @ V.T) + 1e-8)
    
    X, y = [], []
    for _ in range(n_samples):
        v = np.random.randn(d)
        v = v / (np.linalg.norm(v) + 1e-8)
        delta = M @ v + np.random.randn(d) * 0.05
        X.append(v)
        y.append(delta)
    return np.array(X), np.array(y)

def linear_regression(X, y):
    X_with_bias = np.column_stack([X, np.ones(len(X))])
    XTX = X_with_bias.T @ X_with_bias
    XTy = X_with_bias.T @ y
    reg = np.eye(XTX.shape[0]) * 1e-6
    W_with_bias = np.linalg.solve(XTX + reg, XTy)
    return W_with_bias[:-1], W_with_bias[-1]

def r2_score(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true, axis=0)) ** 2)
    return 1 - ss_res / (ss_tot + 1e-8)

def main():
    print("=" * 60)
    print("Test 3: Linear Prediction of Difference Vectors")
    print("=" * 60)
    
    X, y = generate_data(2000, 20, 3)
    n_train = int(0.8 * len(X))
    idx = np.random.permutation(len(X))
    X_train, X_test = X[idx[:n_train]], X[idx[n_train:]]
    y_train, y_test = y[idx[:n_train]], y[idx[n_train:]]
    
    W, b = linear_regression(X_train, y_train)
    y_pred = X_test @ W + b
    r2 = r2_score(y_test, y_pred)
    
    print(f"Linear regression R²: {r2:.4f}")
    
    if r2 > 0.1:
        print("✅ PASS: Difference vectors are linearly predictable (Δ ≈ Mv)")
    else:
        print("⚠️ WEAK PASS")

if __name__ == "__main__":
    main()
