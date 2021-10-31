from typing import List


def dot(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    """Return the dot product of two numerical matrices."""

    ### HELPERS
    def _is_jagged(matrix) -> bool:
        """Verify all rows of the matrix are of the same length."""
        row_lengths = set([len(row) for row in matrix])
        return len(row_lengths) > 1

    def _vector_dot_product(vector1: List[int], vector2: List[int]) -> int:
        v1, v2 = vector1, vector2
        return sum([val1 * val2 for val1, val2 in zip(v1, v2)])

    ### DRIVER
    # A: input validations
    if len(matrix1) == 0:
        raise ValueError("The first matrix is empty, or is uneven.")
    elif len(matrix2) == 0 or len(matrix2[0]) == 0:
        raise ValueError("The second matrix is empty, or is uneven.")
    if _is_jagged(matrix1) is True:
        raise ValueError("The first matrix is uneven.")
    if _is_jagged(matrix2) is True:
        raise ValueError("The second matrix is uneven.")
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Cannot compute dot product of these two matrices.")
    # B: compute the product
    output = list()
    for row1 in matrix1:  # iterate over rows in first matrix
        new_row = list()  # this goes in the output matrix
        for col_index in range(len(matrix2[0])):  # multiply across the cols
            col = [row2[col_index] for row2 in matrix2]
            new_row.append(_vector_dot_product(row1, col))
        output.append(new_row)
    # C: return the product
    return output


if __name__ == "__main__":
    test_cases = [
        # row vector by a column vector
        ([[1, 2]], [[2], [2]]),
        # 2x2 matrix by a column vector
        ([[2, 2], [3, 3]], [[3], [2]]),
    ]
    for mat1, mat2 in test_cases:
        print(dot(mat1, mat2))
