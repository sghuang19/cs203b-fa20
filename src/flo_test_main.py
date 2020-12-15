from matrix import random_matrix_gen
from flo_test import flo_addition_test, flo_multiplication_test
import winsound
from msvcrt import getch

# n = 8192
n = 20
m1 = random_matrix_gen(n)
print("Matrix 1 generation completed")
m2 = random_matrix_gen(n)
print("Matrix 2 generation completed, press any key to continue")
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
getch()

flo_addition_test(m1, m2, n)
print("addition test furnished, press any key to continue")
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
getch()

flo_multiplication_test(m1, m2, n)
print("addition test furnished, press any key to exit")
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
