def square_matrix_multiply(self, a, b):
    """Use the standard approach to multiply 2 matrices a and b, return their product."""
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
    :type elements: List or Tuple
    :type row: int
    :type column: int
    """

        if row is None:
            row = 1
            column = len(elements)
        if column is None:
            column = len(elements) / row

        self.row = row
        self.column = column

        if len(elements) != row * column:
            print('Invalid matrix size')

        self.elements = elements
        self.row = row
        self.column = column


def __str__(self):
    """Convert a matrix to string"""
    return self.elements.__str__()
