"""Tool 4: Path Tracer"""

import numpy as np

def main():
    print("=" * 60)
    print("Tool 4: Path Tracer")
    print("=" * 60)
    
    np.random.seed(42)
    tokens = ["The", "cat", "chases", "the", "mouse"]
    embeddings = np.random.randn(len(tokens), 50)
    
    path = " → ".join(tokens)
    print(f"\nPath: {path}")
    
    print(f"\nStep sizes:")
    total_length = 0
    for i in range(len(embeddings)-1):
        step = np.linalg.norm(embeddings[i+1] - embeddings[i])
        total_length += step
        bar = "█" * min(int(step * 50), 20)
        print(f"  {tokens[i]} → {tokens[i+1]}: {step:.4f} {bar}")
    
    print(f"\nTotal path length: {total_length:.4f}")
    print("\n✅ Path tracer ready")

if __name__ == "__main__":
    main()
