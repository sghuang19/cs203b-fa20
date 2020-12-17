from matrix import Matrix, strassen_multiply

n = 1000
elements = []

for i in range(n * n):
    elements.append(0)
m = Matrix(elements)

strassen_multiply(m, m)

# print("__init__ ran", dimension.count, "times")
# print(f'The function is called: {strassen_multiply.count} times')
