from matrix import *
import time
import random

n = 10000

m1 = random_matrix_gen(n)
m2 = random_matrix_gen(n)

e1 = []
e2 = []
s = 0
for i in range(n):
    e1.append(random.uniform(-1, 1))
    e2.append(random.uniform(-1, 1))
time1 = time.time()
for i in range(n):
    s = e1[i] + e2[i]
time2 = time.time()
alpha = time2 - time1
print(time2 - time1)

time1 = time.time()
for i in range(n):
    s = e1[i] * e2[i]
time2 = time.time()
pi = time2 - time1
print(time2 - time1)

print(alpha / pi)

# m1 = random_matrix_gen(n)
# m2 = random_matrix_gen(n)

# time1 = time.time()
# c = strassen_multiply(m1, m2)
# time2 = time.time()
# print(time2 - time1)
#
# time1 = time.time()
# c1 = square_matrix_multiply(m1, m2)
# time2 = time.time()
# print(time2 - time1)
