import exceptions
import math


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


def strassen_multiply(a, b, n=None):  # for almost square matrix
    """
    Use the Strassen to multiply 2 matrices a and b, return their product.

    :type a: Matrix
    :type b: Matrix
    :type n: int
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
        n = 20
    if max(arow, acol, bcol) < n:  # 100 could be changed to other number depending on input size
        return square_matrix_multiply(a, b)

    half_arow_ceil = math.ceil(arow / 2)
    half_arow_floor = math.floor(arow / 2)
    half_acol_ceil = math.ceil(acol / 2)
    half_acol_floor = math.floor(acol / 2)

    half_brow_ceil = math.ceil(brow / 2)
    half_brow_floor = math.floor(brow / 2)
    half_bcol_ceil = math.ceil(bcol / 2)
    half_bcol_floor = math.floor(bcol / 2)

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

    T2 = adaptiveminus(B1, B3, half_brow_ceil, half_bcol_floor)
    M3 = strassen_multiply(A0, T2)
    C1 = M3
    C3 = adaptiveadd(M3, Matrix([0], 1, 1), half_arow_floor, half_bcol_floor)

    T1 = adaptiveminus(A2, A0, half_arow_ceil, half_acol_ceil)
    T2 = adaptiveadd(B0, B1, half_brow_ceil, half_bcol_ceil)
    M6 = strassen_multiply(T1, T2)
    C3 = adaptiveadd(C3, M6, half_arow_floor, half_bcol_floor)

    T1 = adaptiveadd(A2, A3, half_arow_floor, half_acol_ceil)
    M2 = strassen_multiply(T1, B0)
    C2 = M2
    C3 = adaptiveminus(C3, M2, half_arow_floor, half_bcol_floor)

    T1 = adaptiveadd(A0, A3, half_arow_ceil, half_acol_ceil)
    T2 = adaptiveadd(B0, B3, half_brow_ceil, half_bcol_ceil)
    M1 = strassen_multiply(T1, T2)
    C0 = M1
    C3 = adaptiveadd(C3, M1, half_arow_floor, half_bcol_floor)

    T1 = adaptiveadd(A0, A1, half_arow_ceil, half_acol_floor)
    M5 = strassen_multiply(T1, B3)
    C0 = adaptiveminus(C0, M5, half_arow_ceil, half_bcol_ceil)
    C1 = adaptiveadd(C1, M5, half_arow_ceil, half_bcol_floor)

    T1 = adaptiveminus(A1, A3, half_arow_ceil, half_acol_floor)
    T2 = adaptiveadd(B2, B3, half_brow_floor, half_bcol_ceil)
    M7 = strassen_multiply(T1, T2)
    C0 = adaptiveadd(C0, M7, half_arow_ceil, half_bcol_ceil)

    T2 = adaptiveminus(B2, B0, half_brow_floor, half_bcol_ceil)
    M4 = strassen_multiply(A3, T2)
    C0 = adaptiveadd(C0, M4, half_arow_ceil, half_bcol_ceil)
    C2 = adaptiveadd(C2, M4, half_arow_floor, half_bcol_ceil)

    s = []
    for i in range(C0.row):
        s = s + C0[i + 1:i + 1, 1:C0.col].elements + \
            C1[i + 1:i + 1, 1:C1.col].elements
    for j in range(C2.row):
        s = s + C2[j + 1:j + 1, 1:C2.col].elements + \
            C3[j + 1:j + 1, 1:C3.col].elements
    c = Matrix(s, a.row, b.col)
    return c


def adaptiveadd(a, b, target_row, target_col):
    """
        Given target matrix size, perform adaptive matrix addition
        :type a: Matrix
        :type b: Matrix
        :type target_col: Integer
        :type target_row: Integer
        :return: Matrix
        """
    arow = a.row
    acol = a.col
    brow = b.row
    bcol = b.col
    s = [0] * (target_col * target_row)
    for i in range(target_row):
        for j in range(target_col):
            flag = False
            if 0 <= i < arow and 0 <= j < acol:
                s[i * target_col + j] = a[i + 1, j + 1]
                flag = True
            if 0 <= i < brow and 0 <= j < bcol:
                s[i * target_col + j] = s[i * target_col + j] + b[i + 1, j + 1]
                flag = True
            if not flag:
                s[i * target_col + j] = 0
    c = Matrix(s, target_row, target_col)
    return c


def adaptiveminus(a, b, target_row, target_col):
    """
        Given target matrix size, perform adaptive matrix subtraction
        :type a: Matrix
        :type b: Matrix
        :type target_col: Integer
        :type target_row: Integer
        :return: Matrix
        """
    arow = a.row
    acol = a.col
    brow = b.row
    bcol = b.col
    s = [0] * (target_col * target_row)
    for i in range(target_row):
        for j in range(target_col):
            flag = False
            if 0 <= i < arow and 0 <= j < acol:
                s[i * target_col + j] = a[i + 1, j + 1]
                flag = True
            if 0 <= i < brow and 0 <= j < bcol:
                s[i * target_col + j] = s[i * target_col + j] - b[i + 1, j + 1]
                flag = True
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

    def __init__(self, elements, row=None, col=None):
        """
        Initializes the matrix,

        :param elements: Elements in the matrix, in row-major order
        :param row: The number of rows
        :param col: The number of Columns
        :type row: int
        :type col: int
        """

        if row is None:
            row = 1
            col = len(elements)
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

    def __sizeof__(self):
        return len(self.elements)

    def dimension(self):
        return self.row, self.col
