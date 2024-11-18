class Solution:
    """https://neetcode.io/problems/is-palindrome"""
    def isPalindrome(self, s: str) -> bool:
        """
        Input: str
            - immutable
            - non-empty
            - "printable ASCII" - ?
                - english
                - numbers
                - spaces
                - ASSUME: all the keys on English keyboard
            - even length or odd length

        Output: bool - meets the def of palindrome

        Intuition
            2 ptr

        EC:
            - all spaces --> true

        Approach:

            1) DIY - 2 pointers
                O(n) time, O(1) space
                A: init 2 ptrs

                B: move them both "inward" till both at alphanumeric, stop when they pass each other
                    - make both lower
                    - if equal - keep going
                    - else --> fail fast

                C: return True if loop ends
        """
        ### DRIVER
        # A: init 2 ptrs
        left = l = 0
        right = r = len(s) - 1
        # B: move them both "inward" till both at alphanumeric, stop when they pass each other
        while l <= r:
            while not s[l].isalnum():
                l += 1
            while not s[r].isalnum():
                r -= 1
            # make comparision
            if l <= r:
                # if unequal - fail fast
                if s[l].lower() != s[r].lower():
                    return False
                else:  # TODO[refactor?]
                    l += 1
                    r -= 1
        # C: return True if loop ends
        return True
"""
TESTS
  012345678
 "tab a cat"
    ^
        ^
"""
