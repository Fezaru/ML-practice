import numpy as np

A = [
    [3, 2, 1],
    [2, -1, 4],
    [1, 5, -2],
]

b = [10, 21, -5]

x = np.linalg.solve(A, b)

print(x)
is_correct = np.allclose(np.dot(A, x), b)
print(is_correct)
