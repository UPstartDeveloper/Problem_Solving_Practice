class Matrix:
    """Assumptions based off the problem description, and test cases on
       Exercism: matrix_string only contains positive integers, and the matrix
       has square dimensions.

    """
    def __init__(self, matrix_string):
        """Complexity Analysis:
           Variables:
           n = amount of numbers in each row of the matrix;
                i.e. the values in between newline characters im matrix_string
           m = amount of columns in the matrix;
               i.e. the number of newline characters in matrix_string
           Time: O(n * m), due to the need to account for all the values in
                 matrix, this implementation requires O(n * m) runtime
           Space: O(n * m), because the memory required to build the self.rows
                  and self.cols 2D-arrays grows asymptotically with the size of
                  the input we are given.

        """
        # make a list of the rows
        matrix_lines = matrix_string.splitlines()  # O(n * m)
        self.rows = list()  # O(1)
        for line in matrix_lines:  # O(m)
            # split individual number strings
            line = line.split()  # O(n)
            # convert to numbers, and append to overall list of rows
            row = [int(num) for num in line]  # O(n)
            self.rows.append(row)  # O(1) *amortized

        # make a list of columns
        self.cols = list()  # O(1)
        for i in range(len(row)):  # O(n)
            # iterate over all elements in the same column
            col = [row[i] for row in self.rows]  # O(m)
            self.cols.append(col)  # O(1) *amortized

    def row(self, index):
        """Complexity Analysis
           Time: O(1)
           Space: O(1)

        """
        return self.rows[index - 1]

    def column(self, index):
        """Complexity Analysis
           Time: O(1)
           Space: O(1)

        """
        return self.cols[index - 1]
