"""Tool 2: Local Subspace Viewer"""

import numpy as np
from sklearn.decomposition import PCA

def subspace_dimension(deltas, threshold=0.95):
    if len(deltas) < 2:
        return 1
    pca = PCA()
    pca.fit(deltas)
    cumsum = np.cumsum(pca.explained_variance_ratio_)
    return np.sum(cumsum < threshold) + 1

def main():
    print("=" * 60)
    print("Tool 2: Local Subspace Viewer")
    print("=" * 60)
    
    np.random.seed(42)
    tokens = ["The", "cat", "chases", "the", "mouse"]
    embeddings = np.random.randn(len(tokens), 50)
    
    print(f"\nSliding window analysis (window size=3):")
    print(f"{'Window':<8} {'Token sequence':<25} {'Subspace dimension':<20}")
    print("-" * 55)
    
    for start in range(len(tokens) - 2):
        window_tokens = tokens[start:start+3]
        window_text = ' '.join(window_tokens)
        window_embeds = embeddings[start:start+3]
        deltas = np.array([window_embeds[i+1] - window_embeds[i] for i in range(2)])
        if len(deltas) >= 2:
            dim = subspace_dimension(deltas)
            print(f"[{start}]     {window_text:<25} {dim:<20}")
    
    print("\n✅ Local subspace viewer ready")

if __name__ == "__main__":
    main()
