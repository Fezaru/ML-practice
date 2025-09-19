import matplotlib
matplotlib.use('tkAgg')

import numpy as np
from scipy.sparse import csr_matrix
from matplotlib import pyplot


array = np.zeros((1000, 1000))
for i in range(1000):
    array[i][i] = 1


csr = csr_matrix(array)
density = csr.nnz / (csr.shape[0] * csr.shape[1])
print(density)

pyplot.figure(figsize=(10, 10))
pyplot.spy(csr, markersize=1)
pyplot.xlabel("X")
pyplot.ylabel("Y")
pyplot.grid(True)
pyplot.show()
