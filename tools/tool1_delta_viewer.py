"""Tool 1: Difference Vector Viewer"""

import numpy as np

def get_deltas(embeddings):
    if len(embeddings) < 2:
        return []
    return np.array([embeddings[i+1] - embeddings[i] for i in range(len(embeddings)-1)])

def classify_direction(delta):
    norm = np.linalg.norm(delta)
    if norm < 1e-6:
        return "synonym"
    direction = delta / norm
    if abs(direction[0]) > 0.5:
        return "subject-verb"
    elif abs(direction[1]) > 0.5:
        return "verb-object"
    elif abs(direction[2]) > 0.5:
        return "modifier-head"
    else:
        return "other"

def main():
    print("=" * 60)
    print("Tool 1: Difference Vector Viewer")
    print("=" * 60)
    
    np.random.seed(42)
    tokens = ["The", "cat", "chases", "the", "mouse"]
    embeddings = np.random.randn(len(tokens), 50)
    
    print(f"\nToken sequence: {tokens}")
    print(f"\n{'Step':<4} {'From → To':<20} {'Direction (first 3 dims)':<30} {'Step size':<10} {'Relation':<15}")
    print("-" * 80)
    
    deltas = get_deltas(embeddings)
    for i, delta in enumerate(deltas):
        norm = np.linalg.norm(delta)
        direction = delta / (norm + 1e-8)
        rel_type = classify_direction(delta)
        from_to = f"{tokens[i]} → {tokens[i+1]}"
        dir_str = f"[{direction[0]:6.3f}, {direction[1]:6.3f}, {direction[2]:6.3f}]"
        print(f"{i}→{i+1:<2} {from_to:<20} {dir_str:<30} {norm:.4f}    {rel_type}")
    
    print("\n✅ Difference vector viewer ready")

if __name__ == "__main__":
    main()
