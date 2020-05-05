class Matrix:
    def __init__(self, matrix_string):
        # make a list of the rows
        matrix_lines = matrix_string.splitlines()
        self.rows = list()
        for line in matrix_lines:
            # split individual number strings
            line = line.split()
            # convert to numbers, and append to overall list of rows
            row = [int(num) for num in line]
            self.rows.append(row)

    def row(self, index):
        return self.rows[index]

    def column(self, index):
        pass
