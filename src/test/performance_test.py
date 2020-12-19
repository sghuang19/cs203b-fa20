from Matrix import *
import time

n = 1024

m1 = random_matrix_gen(n)
m2 = random_matrix_gen(n)
print('matrix gen completed')

time1 = time.time()
c = strassen_multiply(m1, m2, 18)
time2 = time.time()
print(time2 - time1)

# time1 = time.time()
# c1 = square_matrix_multiply(m1, m2)
# time2 = time.time()
# print(time2 - time1)
