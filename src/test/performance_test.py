from matrix import Matrix, square_matrix_multiply, strassen_multiply
import time
import random

n = 512

elements = []
for i in range(n * n):
    elements.append(random.uniform(-1, 1))
m1 = Matrix(elements, n, n)

elements = []
for i in range(n * n):
    elements.append(random.uniform(-1, 1))
m2 = Matrix(elements, n, n)

time1 = time.time()
c = strassen_multiply(m1, m2)
time2 = time.time()
print(time2 - time1)

time1 = time.time()
c1 = square_matrix_multiply(m1, m2)
time2 = time.time()
print(time2 - time1)