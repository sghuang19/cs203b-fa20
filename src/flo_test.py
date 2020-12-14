import time
import random

n = 1000000

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
print("the ratio of alpha and pi is", alpha / pi)
