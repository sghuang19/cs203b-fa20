from matrix import random_matrix_gen
from flo_test import flo_test

n = 8192 * 2
m1 = random_matrix_gen(n)
m2 = random_matrix_gen(n)
flo_test(m1, m2, n)
