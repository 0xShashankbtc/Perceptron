import numpy as np

def sgn(t):
    return +1 if t >= 0 else -1

def perceptron_epoch(data, w, b):
    print("Initial parameters: w =", w, ", b =", b)
    print("-" * 50)
    
    updates = []
    
    for i, (x, y) in enumerate(data):
        x = np.array(x)
        score = np.dot(w, x) + b
        y_hat = sgn(score)
        
        if y_hat != y:  # Mistake: update
            w = w + y * x
            b = b + y
            updates.append(i + 1)
            print(f"Point {i+1}: x={x.tolist()}, y={y} --> MISTAKE (y_hat={y_hat})")
            print(f"  UPDATE --> w = {w.tolist()}, b = {b}")
        else:
            print(f"Point {i+1}: x={x.tolist()}, y={y} --> Correct (y_hat={y_hat}), no update")
            print(f"  No change --> w = {w.tolist()}, b = {b}")
        print()
    
    print("=" * 50)
    print(f"Final w = {w.tolist()}, b = {b}")
    print(f"Points that caused updates: {updates}")
    return w, b

# Dataset
data = [
    ([1,  1],  +1),
    ([-1, -2], -1),
    ([2, -1],  -1),
    ([0,  2],  +1),
]

# Initialization
w = np.array([0.0, 0.0])
b = 0.0

perceptron_epoch(data, w, b)
