from matrix import Matrix
from matrix import strassen_mutliply
import numpy as np

elements = [1, 2, 3, 4, 5, 6]
a1 = np.array(range(16)).reshape(4,4)
a2 = np.array(range(16)).reshape(4,4)

m1 = Matrix(range(16),4,4)
m2 = Matrix(range(16),4,4)
#print(list(m1[1:1,1:m1.column]))
c = strassen_mutliply(m1,m2)
c2 = np.dot(a1,a2)
print(c)
print(c2)

