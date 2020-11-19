class RowOutOfBoundsException(Exception):
    def __init__(self, index):
        err = 'The row index out of bounds:{0}'.format(index)
        Exception.__init__(self, err)


class ColumnOutOfBoundsException(Exception):
    def __init__(self, index):
        err = 'The column index  out of bounds:{0}'.format(index)
        Exception.__init__(self, err)


class IndexOutOfBoundsException(Exception):
    def __init__(self, index):
        err = 'The index  out of bounds:{0}'.format(index)
        Exception.__init__(self, err)


class DimensionInconsistentException(Exception):
    def __init__(self):
        err = 'The dimension of operands is inconsistent'
        Exception.__init__(self, err)


class InvalidElementException(Exception):
    def __init__(self):
        err = 'The dimension of the operand matrices is inconsistent'
        Exception.__init__(self, err)
