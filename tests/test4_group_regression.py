"""Test 4: Group Regression"""

import numpy as np

np.random.seed(42)

def generate_mixed_data(n_per_class=500, d=20, rank=3, n_classes=3):
    X, y, labels = [], [], []
    for c in range(n_classes):
        U = np.random.randn(d, rank)
        V = np.random.randn(d, rank)
        M = np.eye(d) + (U @ V.T) * 0.3 / (np.linalg.norm(U @ V.T) + 1e-8)
        for _ in range(n_per_class):
            v = np.random.randn(d)
            v = v / (np.linalg.norm(v) + 1e-8)
            delta = M @ v + np.random.randn(d) * 0.05
            X.append(v)
            y.append(delta)
            labels.append(c)
    return np.array(X), np.array(y), np.array(labels)

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
    print("Test 4: Group Regression")
    print("=" * 60)
    
    X, y, labels = generate_mixed_data(500, 20, 3, 3)
    
    W_global, b_global = linear_regression(X, y)
    y_pred_global = X @ W_global + b_global
    r2_global = r2_score(y, y_pred_global)
    
    r2_per_class = []
    for c in range(3):
        mask = labels == c
        W_c, b_c = linear_regression(X[mask], y[mask])
        y_pred_c = X[mask] @ W_c + b_c
        r2_c = r2_score(y[mask], y_pred_c)
        r2_per_class.append(r2_c)
    
    avg_r2 = np.mean(r2_per_class)
    
    print(f"Global R²: {r2_global:.4f}")
    print(f"Group average R²: {avg_r2:.4f}")
    print(f"Improvement: {avg_r2 - r2_global:.4f}")
    
    if avg_r2 > r2_global + 0.1:
        print("✅ PASS: Different relations need different linear maps")
    else:
        print("⚠️ WEAK PASS")

if __name__ == "__main__":
    main()
