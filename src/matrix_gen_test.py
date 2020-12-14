import time
from matrix import Matrix, square_matrix_multiply
from matrix import strassen_multiply
import numpy as np

elements = [1, 2, 3, 4, 5, 6]
a1 = np.array(range(16)).reshape(4, 4)
a2 = np.array(range(16)).reshape(4, 4)

m1 = Matrix(range(16), 4, 4)
m2 = Matrix(range(16), 4, 4)
# print(list(m1[1:1,1:m1.column]))
c = strassen_multiply(m1, m2)
c2 = np.dot(a1, a2)
print(c)
print(c2)


m1 = Matrix(range(10000), 100, 100)
m2 = Matrix(range(10000), 100, 100)
# print(list(m1[1:1,1:m1.column]))
time1 = time.time()
c = strassen_multiply(m1, m2)
time2 = time.time()
print(time2-time1)

time1 = time.time()
c1 = square_matrix_multiply(m1, m2)
time2 = time.time()
print(time2-time1)

# print(c1 - c)
# print(c1)
# print(c)
