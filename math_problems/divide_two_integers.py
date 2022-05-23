class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """LeetCode: https://leetcode.com/problems/divide-two-integers/"""
        # set return value + params
        quotient = q = 0
        are_same_symbol = (dividend > 0 and divisor > 0) or (
            dividend < 0 and divisor < 0
        )
        is_subtract = 1 if are_same_symbol else -1

        # EC
        if dividend == 0:
            return 0

        # compute q
        remainder = r = dividend
        while abs(r) >= abs(divisor):
            r = r - (is_subtract * divisor)
            q += 1

        if are_same_symbol:
            return q
        return q * -1
