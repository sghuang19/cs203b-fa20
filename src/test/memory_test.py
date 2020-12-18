import sys

from Matrix import *
import time

n = 128
print('matrix gen start')
m1 = random_matrix_gen(n)
m2 = random_matrix_gen(n)
print('matrix gen completed')

print('start')
c = strassen_multiply(m1, m2, 128)
sys.exit(0)
print('test')
# time1 = time.time()
# c1 = square_matrix_multiply(m1, m2)
# time2 = time.time()
# print(time2 - time1)
