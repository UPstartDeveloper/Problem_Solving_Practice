class Solution:
    """https://neetcode.io/problems/spiral-matrix"""
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # go as far right as possible
            for i in range(left, right):
                res.append(matrix[top][i])
            # now that this row is done, move down
            top += 1
            # go as far down as possible
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            # now this col is done, move left
            right -= 1
            # do the boundaries don't overlap yet - if so we're done
            if not (left < right and top < bottom):
                break
            # go left as much as possible
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            # this row is done, so move up
            bottom -= 1
            # go up as much as possible
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            # this col is done, move right
            left += 1

        return res
