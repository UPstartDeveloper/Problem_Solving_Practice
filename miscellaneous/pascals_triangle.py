def pascal_triangle(num_rows):
    # init list for all the rows
    rows = list([list() for _ in range(num_rows)])
    # create the rows
    for row_index in range(num_rows):
        # A: at each index in the overall matrix, create an array as long as that
        # row position
        new_row = list([1 for i in range(row_index + 1)])
        # B: fill in the in-between elements
        previous_row = rows[row_index - 1]
        for column_index in range(1, len(new_row) - 1):
            # at each index, sum the elements in prev[index] + prev[index - 1]
            new_row[column_index] = (
                previous_row[column_index] + previous_row[column_index - 1]
            )
        print(new_row)
        rows[row_index] = new_row
    return rows


if __name__ == "__main__":
    rows = 6
    pascal_triangle(rows)
