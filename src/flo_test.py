import time
from matrix import random_matrix_gen

n = 8192

e1 = random_matrix_gen(n)
e2 = random_matrix_gen(n)

print("benchmark starts")

time1 = time.time()
for i in range(n * n):
    s = e1[i] + e2[i]
time2 = time.time()
alpha = time2 - time1
print(time2 - time1)

time1 = time.time()
for i in range(n * n):
    s = e1[i] * e2[i]
time2 = time.time()
pi = time2 - time1
print(time2 - time1)

print("the ratio of alpha and pi is ", pi / alpha)
