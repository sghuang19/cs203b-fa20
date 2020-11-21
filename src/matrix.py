import exceptions


def square_matrix_multiply(a, b):
    """
    Use the standard approach to multiply 2 matrices a and b, return their product.

    :type a: Matrix
    :type b: Matrix
    :return: Matrix
    """
    # TODO(SamuelHuang2019): Finish the docstring.
    print('Hello World!')


class Matrix:
    """
    A data structure for matrix. The matrix implementation should be suitable for dense matrices. You are required to
    define a class Matrix that will be used in the implementation. This class Matrix will represent a matrix in
    “row-major” order (i.e. for an n×n-matrix the first row will be stored in an array at index 0 to index n-1 the
    next row at n to 2n-1 and so on). The class should provide a constructor and methods to get and set the element
    at any row column index.

    # :type __elements: list, default [0.0]
    # :type __row: int, default 1
    # :type __column: int, default 1

    """

    # TODO(SamuelHuang2019): Finish the docstring.
    # TODO(SamuelHuang2019): More methods.

    def __init__(self, elements, row=None, column=None):
        """
        Initializes the matrix,

        :param elements: Elements in the matrix, in row-major order
        :param row: The number of rows
        :param column: The number of Columns
        :type row: int
        :type column: int
        """

        if row is None:
            row = 1
            column = len(elements)
        if column is None:
            column = len(elements) // row

        self.row = row
        self.column = column

        if len(elements) is not row * column:
            print('Invalid matrix size')

        self.elements = elements
        self.row = row
        self.column = column

    def __str__(self):
        """Convert a matrix to string"""
        result = ''
        for i in range(self.row):
            for j in range(self.column):
                result = result + ' ' + str(self.__getitem__((i + 1, j + 1)))
                if j == self.column - 1:
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
                row_range = range(row_indices[0], row_indices[1] + 1, row_indices[2])
                col_indices = item[1].indices(self.column)
                col_range = range(col_indices[0], col_indices[1] + 1, col_indices[2])
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
            if isinstance(item[0], slice) and isinstance(item[1], slice):
                return

            # one slice, one int
            if isinstance(item[0], slice) and isinstance(item[1], slice):
                return

            # both of the elements in the item are int
            if item[0] > self.row or item[0] <= 0:
                raise (exceptions.RowOutOfBoundsException(item))
            if item[1] > self.column or item[1] <= 0:
                raise (exceptions.ColumnOutOfBoundsException(item))
            return self.elements[(item[0] - 1) * self.column + item[1] - 1]

        # for slice input
        if isinstance(item, slice):
            return self.elements[item]

        # else for int input
        if item >= len(self.elements):
            raise (exceptions.ColumnOutOfBoundsException(item))
        return self.elements[item]

    def __add__(self, other):
        """
        :rtype: Matrix
        """

        if type(other) is Matrix:
            if self.row is other.row and self.column is other.column:
                s = []
                for i in range(len(self.elements)):
                    s += [self.elements[i] + other.elements[i]]
                return Matrix(s, self.row, self.column)
            raise (exceptions.DimensionInconsistentException())

        for i in range(len(self.elements)):
            self.elements[i] += other
        return self

    def __sizeof__(self):
        return len(self.elements)

    def dimension(self):
        return self.row, self.column
