import numpy as np


def transpose(matrix: np.ndarray) -> np.ndarray:
    return np.array(list(zip(*matrix)))


def add(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    assert matrix1.shape == matrix2.shape, "Matrix must have equal shape"
    return np.array(list([a + b for a, b in zip(r1, r2)]
                     for r1, r2 in zip(matrix1, matrix2)))


def multiply(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    m, n = matrix1.shape
    n2, p = matrix2.shape
    assert n == n2, "Matrix 1 col size shall be equal matrix 2 row size"
    matrix2_cols = transpose(matrix2)
    result = []
    for i, row in enumerate(matrix1):
        result.append([])
        for j, col in enumerate(matrix2_cols):
            element_result = 0
            for k in range(len(row)):
                element_result += row[k] * col[k]
            result[i].append(element_result)
    return np.asarray(result)


a = np.array([
    [1, 2, 3],
    [5, 6, 7],
])
b = np.array([
    [1, 1, 1],
    [1, 1, 1],
])
c = np.array([
    [2, 2],
    [2, 2],
    [2, 2],
])

print(transpose(a))
print(add(a, b))
print(multiply(b, c))
