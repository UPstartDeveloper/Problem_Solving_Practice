from typing import List


class Solution:
    def longest_increasing_path(self, nums: List[int], left: int, right: int) -> int:
        """
        Source: https://interviewing.io/recordings/Java-FAANG-12

        Given an int[] nums and 2 int's left and right, 
        return the number of non-empty subarrays whose max is left <= max <= right.

        Example:
            in: [2, 1, 4, 3], left = 2, right = 3
            out: 3

            explanation: our subarrays are [2], [2, 1], and [3]

        Input:
            nums: immutable, any ints, unsorted, dupes allowed
            left, right: any int

        EC:
            left > right --> switch 'em
            nums = [] --> return 0

        Intuition:
            DP?

        BCR: O(n) time, O(1) space
        
        """
        ### HELPERS
        ...

        ### EC
        if not left <= right:
            left, right = right, left
        if len(nums) == 0:
            return 0

        ### DRIVER
        largest, count = float("-inf"), 0

        for num in nums:
            old_largest_in_range = left <= largest <= right
            # best case - both values between left/right
            if left <= num <= right:
                if old_largest_in_range:
                    count += 2
                else:
                    count += 1
                # update largest
                if largest > right:
                    largest = min(right, num)
                elif largest < left:
                    largest = max(left, num)
                else:  # left <= largest <= right
                    largest = max(largest, num)
            # conditional case - we may add subarrs
            elif num < left:
                if old_largest_in_range:
                    count += 1
            # negative case - cannot add subarrs, only update largest
            else:  # num > right
                largest = max(num, largest)

            print(f"count is now {count}, largest is {largest}, num is {num}")

        return count


if __name__ == "__main__":
    inputs = (
        # ([2, 1, 4, 3], 2, 3),
        # ([2, 4, 1, 4, 3, 4, 3], 2, 3),
        ([2, 1, 3, 4, 3], 2, 3),
    )
    correct_outputs = [6]

    sol = Solution()

    for input, output in zip(inputs, correct_outputs):
        arr, left, right = input
        real = sol.longest_increasing_path(arr, left, right)
        assert (
            sol.longest_increasing_path(arr, left, right) == output
        ), f"expected {output}, received {real}"
