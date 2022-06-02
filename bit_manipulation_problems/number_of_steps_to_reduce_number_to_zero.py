class Solution:
    """LeetCode: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/"""

    def numberOfSteps(self, num: int) -> int:
        if not isinstance(num, int) or num < 0:
            raise ValueError(f"value {num} is not an int > 0")

        steps = 0

        bits = bin(num)[2:]

        for bit in bits:
            if bit == "0":
                steps += 1
            else:  # bit is 1
                steps += 2

        return steps - 1  # readjust, b/c last 0 doesn't need to go away
