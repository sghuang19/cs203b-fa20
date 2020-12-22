# coding: utf-8
from memory_profiler import profile
import exceptions
import math
# from CallingCounter import CallingCounter

import random


def random_matrix_gen(m, n=None):
    """
    Generates a random matrix of size n by n, the elements are randomly from -1 to 1 float number.
    :param m: optional dimension
    :param n: the size of the matrix
    :type m: int
    :type n: int
    :return: The generated random matrix
    :rtype Matrix
    """
    n = m if n is None else n
    elements = []
    for i in range(m * n):
        elements.append(random.uniform(-1, 1))
    return Matrix(elements, m, n)


# @profile
def square_matrix_multiply(a, b):
    """
    Use the standard approach to multiply 2 matrices a and b, return their product.

    :type a: Matrix
    :type b: Matrix
    :return: Matrix
    """
    if a.col != b.row:
        print("Unmatched matrix size")
        return
    s = [0] * (a.row * b.col)
    for i in range(a.row):
        for j in range(b.col):
            for k in range(a.col):
                s[i * b.col + j] = s[i * b.col + j] + \
                                   a[i + 1, k + 1] * b[k + 1, j + 1]
    c = Matrix(s, a.row, b.col)
    return c


# @profile
def strassen_multiply(a, b, n=None):  # for almost square matrix
    """
    Use the Strassen to multiply 2 matrices a and b, return their product.

    :param n:
    :type a: Matrix
    :type b: Matrix
    :return: Matrix
    """
    arow = a.row
    acol = a.col
    brow = b.row
    bcol = b.col
    if acol != brow:
        print("Unmatched matrix size")
        return

    if n is None:
        n = 46

    if max(arow, acol, bcol) < 100:  # 100 could be changed to other number depending on input size
        return square_matrix_multiply(a, b)

    # Ceil and floor number for matrix a
    half_arow_ceil = math.ceil(arow / 2)
    half_arow_floor = math.floor(arow / 2)
    half_acol_ceil = math.ceil(acol / 2)
    half_acol_floor = math.floor(acol / 2)

    # Ceil and floor number for matrix b
    half_brow_ceil = math.ceil(brow / 2)
    half_brow_floor = math.floor(brow / 2)
    half_bcol_ceil = math.ceil(bcol / 2)
    half_bcol_floor = math.floor(bcol / 2)

    # Divide matrix a and b into 4 submatrix.
    A0 = a[1:half_arow_ceil, 1:half_acol_ceil]
    A1 = a[1:half_arow_ceil, half_acol_ceil +
                             1:half_acol_ceil + half_acol_floor]
    A2 = a[half_arow_ceil + 1:half_arow_ceil +
                              half_arow_floor, 1:half_acol_ceil]
    A3 = a[half_arow_ceil + 1:half_arow_ceil + half_arow_floor,
         half_acol_ceil + 1:half_acol_ceil + half_acol_floor]
    B0 = b[1:half_brow_ceil, 1:half_bcol_ceil]
    B1 = b[1:half_brow_ceil, half_bcol_ceil +
                             1:half_bcol_ceil + half_bcol_floor]
    B2 = b[half_brow_ceil + 1:half_brow_ceil +
                              half_brow_floor, 1:half_bcol_ceil]
    B3 = b[half_brow_ceil + 1:half_brow_ceil + half_brow_floor,
         half_bcol_ceil + 1:half_bcol_ceil + half_bcol_floor]

    T2 = adaptive_minus(B1, B3, half_brow_ceil, half_bcol_floor)  # T2 = B1 - B3
    M3 = strassen_multiply(A0, T2)  # M3 = A0 *s T2
    C1 = M3  # C1 = M3
    C3 = adaptive_add(M3, Matrix([0], 1, 1), half_arow_floor, half_bcol_floor)  # C3 = M3

    T1 = adaptive_minus(A2, A0, half_arow_ceil, half_acol_ceil)  # T1 = A2 - A0
    T2 = adaptive_add(B0, B1, half_brow_ceil, half_bcol_ceil)  # T2 = B0 + B1
    M6 = strassen_multiply(T1, T2)  # M6 = T1 *s T2
    C3 = adaptive_add(C3, M6, half_arow_floor, half_bcol_floor)  # C3 = C3 + M6

    T1 = adaptive_add(A2, A3, half_arow_floor, half_acol_ceil)  # T1 = A2 + A3
    M2 = strassen_multiply(T1, B0)  # M2 = T1 *s B0
    C2 = M2  # C2 = M2
    C3 = adaptive_minus(C3, M2, half_arow_floor, half_bcol_floor)  # C3 = C3 - M2

    T1 = adaptive_add(A0, A3, half_arow_ceil, half_acol_ceil)  # T1 = A0 + A3
    T2 = adaptive_add(B0, B3, half_brow_ceil, half_bcol_ceil)  # T2 = B0 + B3
    M1 = strassen_multiply(T1, T2)  # M1 = T1 *s T2
    C0 = M1  # C0 = M1
    C3 = adaptive_add(C3, M1, half_arow_floor, half_bcol_floor)  # C3 = C3 + M1

    T1 = adaptive_add(A0, A1, half_arow_ceil, half_acol_floor)  # T1 = A0 + A1
    M5 = strassen_multiply(T1, B3)  # M5 = T1 *s B3
    C0 = adaptive_minus(C0, M5, half_arow_ceil, half_bcol_ceil)  # C0 = C0 - M5
    C1 = adaptive_add(C1, M5, half_arow_ceil, half_bcol_floor)  # C1 = C1 + M5

    T1 = adaptive_minus(A1, A3, half_arow_ceil, half_acol_floor)  # T1 = A1 - A3
    T2 = adaptive_add(B2, B3, half_brow_floor, half_bcol_ceil)  # T2 = B2 + B3
    M7 = strassen_multiply(T1, T2)  # M7 = T1 *s T2
    C0 = adaptive_add(C0, M7, half_arow_ceil, half_bcol_ceil)  # C0 = C0 + M7

    T2 = adaptive_minus(B2, B0, half_brow_floor, half_bcol_ceil)  # T2 = B2 - B0
    M4 = strassen_multiply(A3, T2)  # M4 = A3 *s T2
    C0 = adaptive_add(C0, M4, half_arow_ceil, half_bcol_ceil)  # C0 = C0 + M4
    C2 = adaptive_add(C2, M4, half_arow_floor, half_bcol_ceil)  # C2 = C2 + M4

    # Join submatrix C0, C1, C2 and C3
    s = []
    for i in range(C0.row):  # Join C0 and C1
        s = s + C0[i + 1:i + 1, 1:C0.col].elements + \
            C1[i + 1:i + 1, 1:C1.col].elements
    for j in range(C2.row):  # Join C2 and C3
        s = s + C2[j + 1:j + 1, 1:C2.col].elements + \
            C3[j + 1:j + 1, 1:C3.col].elements
    c = Matrix(s, a.row, b.col)
    return c


# @profile
def adaptive_add(a, b, target_row, target_col):
    """
        Given target matrix size, perform adaptive matrix addition
        :type a: Matrix
        :type b: Matrix
        :type target_col: Integer
        :type target_row: Integer
        :return: Matrix
        """

    # number of row and column
    arow = a.row
    acol = a.col
    brow = b.row
    bcol = b.col

    s = [0] * (target_col * target_row)
    for i in range(target_row):
        for j in range(target_col):
            flag = False  # Used as the condition of padding zero
            # Perform element wise addition if i and j are within the size of matrix a and b
            if 0 <= i < arow and 0 <= j < acol:
                s[i * target_col + j] = a[i + 1, j + 1]
                flag = True
            if 0 <= i < brow and 0 <= j < bcol:
                s[i * target_col + j] = s[i * target_col + j] + b[i + 1, j + 1]
                flag = True
            # If i or j goes beyond the size of a and b, pad zero.
            if not flag:
                s[i * target_col + j] = 0
    c = Matrix(s, target_row, target_col)
    return c


# @profile
def adaptive_minus(a, b, target_row, target_col):
    """
        Given target matrix size, perform adaptive matrix subtraction
        :type a: Matrix
        :type b: Matrix
        :type target_col: Integer
        :type target_row: Integer
        :return: Matrix
        """

    # number of row and column
    arow = a.row
    acol = a.col
    brow = b.row
    bcol = b.col

    s = [0] * (target_col * target_row)
    for i in range(target_row):
        for j in range(target_col):
            flag = False    # Used as the condition of padding zero
            # Perform element wise subtraction if i and j are within the size of matrix a and b
            if 0 <= i < arow and 0 <= j < acol:
                s[i * target_col + j] = a[i + 1, j + 1]
                flag = True
            if 0 <= i < brow and 0 <= j < bcol:
                s[i * target_col + j] = s[i * target_col + j] - b[i + 1, j + 1]
                flag = True
            # If i or j goes beyond the size of a and b, pad zero.
            if not flag:
                s[i * target_col + j] = 0
    c = Matrix(s, target_row, target_col)
    return c


class Matrix:
    """
    A data structure for matrix. The matrix implementation should be suitable for dense matrices. You are required to
    define a class Matrix that will be used in the implementation. This class Matrix will represent a matrix in
    “row-major” order (i.e. for an n×n-matrix the first row will be stored in an array at index 0 to index n-1 the
    next row at n to 2n-1 and so on). The class should provide a constructor and methods to get and set the element
    at any row column index.

    # :type __elements: list, default [0.0]
    # :type __row: int, default 1
    # :type __col: int, default 1

    """

    # TODO(SamuelHuang2019): Finish the docstring.
    # TODO(SamuelHuang2019): More methods.

    def __init__(self, elements, row=1, col=None):
        """
        Initializes the matrix,

        :param elements: Elements in the matrix, in row-major order
        :param row: The number of rows
        :param col: The number of Columns
        :type row: int
        :type col: int
        """

        if col is None:
            col = len(elements) // row

        # print(row)
        # print(column)
        # print(len(elements))
        if len(elements) != row * col:
            print('Invalid matrix size')

        self.elements = elements
        self.row = row
        self.col = col

    def __str__(self):
        """Convert a matrix to string"""
        result = ''
        for i in range(self.row):
            for j in range(self.col):
                result = result + ' ' + str(self.__getitem__((i + 1, j + 1)))
                if j == self.col - 1:
                    result = result + '\n'
        return result

    # @profile
    def __getitem__(self, item):
        """
        Get element with index of key, in row-major order
        Index of col or row starts from 1
        """

        # for tuple input
        if isinstance(item, tuple):
            # both of the elements in the item are slice
            if isinstance(item[0], slice) and isinstance(item[1], slice):
                e = []
                row_indices = item[0].indices(self.row)
                row_range = range(
                    row_indices[0], row_indices[1] + 1, row_indices[2])
                col_indices = item[1].indices(self.col)
                col_range = range(
                    col_indices[0], col_indices[1] + 1, col_indices[2])
                r = 0
                c = 0
                for i in row_range:
                    r += 1
                    c = 0
                    for j in col_range:
                        c += 1
                        e += [self[i, j]]
                return Matrix(e, r, c)

            # one slice, one int
            # both of the elements in the item are int
            if isinstance(item[0], int) and isinstance(item[1], int):
                if item[0] > self.row or item[0] <= 0:
                    raise (exceptions.RowOutOfBoundsException(item))
                if item[1] > self.col or item[1] <= 0:
                    raise (exceptions.ColumnOutOfBoundsException(item))
                return self.elements[(item[0] - 1) * self.col + item[1] - 1]

        # # for slice input
        # if isinstance(item, slice):
        #     return self.elements[item]

        # else for int input
        if isinstance(item, int):
            if item > len(self.elements):
                raise (exceptions.ColumnOutOfBoundsException(item))
            return self.elements[item - 1]

    # @profile
    def __add__(self, other):
        """
        If other is a matrix, perform matrix addition, else perform addition with a number element-wisely

        :rtype: Matrix
        """

        if type(other) is Matrix:
            if self.row is other.row and self.col is other.col:
                s = []
                for i in range(len(self.elements)):
                    s += [self.elements[i] + other.elements[i]]
                return Matrix(s, self.row, self.col)
            raise (exceptions.DimensionInconsistentException())

        for i in range(len(self.elements)):
            self.elements[i] += other
        return self

    # @profile
    def __sub__(self, other):
        """
        If other is a matrix, perform matrix subtraction, else perform subtraction with a number element-wisely

        :rtype: Matrix
        """
        if type(other) is Matrix:
            if self.row is other.row and self.col is other.col:
                s = []
                for i in range(len(self.elements)):
                    s += [self.elements[i] - other.elements[i]]
                return Matrix(s, self.row, self.col)
            raise (exceptions.DimensionInconsistentException())

        for i in range(len(self.elements)):
            self.elements[i] -= other
        return self

    # @profile
    def __sizeof__(self):
        return len(self.elements)

    def dimension(self):
        return self.row, self.col
