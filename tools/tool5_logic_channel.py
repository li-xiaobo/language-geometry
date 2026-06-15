"""Tool 5: Probability-Logic Channel"""

import numpy as np

def delta_to_implication(delta, temperature=0):
    norm = np.linalg.norm(delta)
    if temperature == 0:
        if norm < 0.01:
            return "↔ (equivalence)"
        else:
            return "→ (implication)"
    else:
        prob = min(1.0, norm / 0.05)
        return f"→ (p={prob:.2f})"

def main():
    print("=" * 60)
    print("Tool 5: Probability-Logic Channel")
    print("=" * 60)
    
    np.random.seed(42)
    tokens = ["cat", "chases", "mouse"]
    embeddings = np.random.randn(len(tokens), 50)
    
    deltas = [embeddings[1]-embeddings[0], embeddings[2]-embeddings[1]]
    
    print(f"\nReasoning chain (T=0, deterministic logic):")
    for i, delta in enumerate(deltas):
        impl = delta_to_implication(delta, temperature=0)
        print(f"  {tokens[i]} {impl} {tokens[i+1]}")
    
    if len(deltas) >= 2:
        print(f"\nComposite (hypothetical syllogism):")
        total_delta = np.sum(deltas, axis=0)
        impl_total = delta_to_implication(total_delta, temperature=0)
        print(f"  {tokens[0]} {impl_total} {tokens[-1]}")
    
    print("\n✅ Probability-logic channel ready")

if __name__ == "__main__":
    main()
