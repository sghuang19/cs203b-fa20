class RowOutOfBoundsException(Exception):
    def __init__(self, parameter, para_value):
        err = 'The row index "{0}"[0] out of bounds:{1}'.format(parameter, para_value)
        Exception.__init__(self, err)
        self.parameter = parameter
        self.para_value = para_value


class ColumnOutOfBoundsException(Exception):
    def __init__(self, parameter, para_value):
        err = 'The column index "{0}"[1] out of bounds:{1}'.format(parameter, para_value)
        Exception.__init__(self, err)
        self.parameter = parameter
        self.para_value = para_value


class IndexOutOfBoundsException(Exception):
    def __init__(self, parameter, para_value):
        err = 'The index "{0}" out of bounds:{1}'.format(parameter, para_value)
        Exception.__init__(self, err)
        self.parameter = parameter
        self.para_value = para_value


class DimensionInconsistentException(Exception):
    def __init__(self):
        err = 'The dimension of operands is inconsistent'
        Exception.__init__(self, err)


class InvalidElementException(Exception):
    def __init__(self):
        err = 'The dimension of the operand matrices is inconsistent'
        Exception.__init__(self, err)
