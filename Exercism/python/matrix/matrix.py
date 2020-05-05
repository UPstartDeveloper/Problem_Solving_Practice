class Matrix:
    """Assumptions based off the problem description, and test cases on
       Exercism: matrix_string only contains positive integers, and the matrix
       has square dimensions.

    """
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

        # make a list of columns
        self.cols = list()
        for i in range(len(row)):
            # iterate over all elements in the same column
            col = [row[i] for row in self.rows]
            self.cols.append(col)

    def row(self, index):
        print(self.rows)
        return self.rows[index - 1]

    def column(self, index):
        return self.cols[index - 1]
