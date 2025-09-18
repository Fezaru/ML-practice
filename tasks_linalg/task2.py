import numpy as np


def check_is_matrix_symmetric(matrix: np.ndarray) -> bool:
    assert matrix.shape[0] == matrix.shape[1], "Matrix must be square"
    matrixT = matrix.T
    return np.array_equal(matrix, matrixT)


def check_is_matrix_orthogonal(matrix: np.ndarray) -> bool:
    assert matrix.shape[0] == matrix.shape[1], "Matrix must be square"
    return np.array_equal(matrix @ matrix.T, np.identity(matrix.shape[0]))


def check_is_matrix_diagonal(matrix: np.ndarray) -> bool:
    assert matrix.shape[0] == matrix.shape[1], "Matrix must be square"
    sum_main_diagonal = sum([matrix[i][i] for i in range(matrix.shape[0])])
    return matrix.sum() - sum_main_diagonal == 0


a = np.array([  # symmetric
    [1, 1],
    [1, 1],
])
b = np.array([  # none
    [1, 2],
    [4, 5],
])
c = np.array([[0, 1, 0, 0],  # orthogonal
              [0, 0, 1, 0],
              [0, 0, 0, 1],
              [1, 0, 0, 0]])
d = np.array([  # diagonal
    [1, 0],
    [0, 1],
])


print(check_is_matrix_symmetric(a))
print(check_is_matrix_symmetric(b))

print(check_is_matrix_orthogonal(c))
print(check_is_matrix_orthogonal(b))

print(check_is_matrix_diagonal(d))
print(check_is_matrix_diagonal(b))
