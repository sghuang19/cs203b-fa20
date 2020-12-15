import time
from matrix import random_matrix_gen

n = 8192
m1 = random_matrix_gen(n)
m2 = random_matrix_gen(n)

time1 = time.time()
for i in range(n * n):
    s = m1[i] * m2[i]
time2 = time.time()

print(time2 - time1)
