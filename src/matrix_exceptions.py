class RowOutOfBoundException(Exception):
    def __init__(self, parameter, para_value):
        err = 'The row index "{0}"[0] out of bounds:{1}'.format(parameter, para_value)
        Exception.__init__(self, err)
        self.parameter = parameter
        self.para_value = para_value


class ColumnOutOfBoundException(Exception):
    def __init__(self, parameter, para_value):
        err = 'The column index "{0}"[1] out of bounds:{1}'.format(parameter, para_value)
        Exception.__init__(self, err)
        self.parameter = parameter
        self.para_value = para_value


class IndexOutOfBoundException(Exception):
    def __init__(self, parameter, para_value):
        err = 'The index "{0}" out of bounds:{1}'.format(parameter, para_value)
        Exception.__init__(self, err)
        self.parameter = parameter
        self.para_value = para_value
