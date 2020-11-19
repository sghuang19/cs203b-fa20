def square_matrix_multiply(self, a, b):
    """Use the standard approach to multiply 2 matrices a and b, return their product."""
    # TODO(SamuelHuang2019): Finish the docstring.





import matrix_exceptions


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
        result = ''
        for i in range(self.row):
            for j in range(self.column):
                result = result + ' '+str(self.__getitem__((i+1,j+1)))
                if j == self.column-1:
                    result = result + '\n'
        return result

    def __getitem__(self, item):
        """
        Get element with index of key, in row-major order
        Index of col or row starts from 1
        """
        if type(item) is tuple:
            if item[0] > self.row or item[0] <= 0:
                raise (matrix_exceptions.RowOutOfBoundException(item, item[0]))
            if item[1] > self.column or item[1] <= 0:
                raise (matrix_exceptions.ColumnOutOfBoundException(item, item[1]))
            return self.elements[(item[0]-1)*self.column + item[1]-1]

        if item >= len(self.elements):
            raise (matrix_exceptions.ColumnOutOfBoundException(item, item))
            return self.elements[item]

