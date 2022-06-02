class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        O(n*k) time, O(2**k) space
        LeetCode: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
        """
        all_substrs, all_codes = set(), (2 ** k)

        # TODO-optimize: use bits as base10, slide across for unique
        for index in range(0, len(s) - k + 1):
            substr = s[index : index + k]
            all_substrs.add(substr)

            # early exit
            if len(all_substrs) == all_codes:
                return True

        # final answer
        return len(all_substrs) == all_codes
