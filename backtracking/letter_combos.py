class Solution:
    # A: digit --> letter mappings
    digit_letters = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        """
        in == out in len

        empty string

        2-9 ONLY

        in order for sure

        Intutiom: ==> want all the perm

        Approach:

        1. Four nested loops
          - init out == []

            - check for the digit
            - iterate through digit_letter combos
            - once a full perm --> out

         - return out
         # --------------------------
         {
            "2": ["a", "b", "c"]
            "3": ["d", "e", "f"]
         }

        o = ["ad", "ae", "af", "bd"]

        1st --- ["a", "b", "c"]
                       ^
        2nd --> ["d", "e", "f"]
                  ^

        [
            ["a", "b", "c"],
            ["d", "e", "f"]
        ]
        Edge Cases:
        "" --> []
        spaces --> N/A
        1 or 0 --> N/A

        """

        def form_perms(digit_ndx, current_perm, all_perms):
            if digit_ndx < len(digits):
                # define the letters we're iterating over
                digit = digits[digit_ndx]
                letters = self.digit_letters[digit]
                # add the letters from this level of the call tree
                for letter in letters:
                    current_perm.append(letter)
                    if len(current_perm) == len(digits):
                        all_perms.append("".join(current_perm))
                    # move on to the next level of the tree
                    form_perms(digit_ndx + 1, [l for l in current_perm], all_perms)
                    current_perm.pop()

        #######################################

        # B: form all the perms
        all_perms, current_perm = list(), list()
        digit_ndx = 0
        form_perms(digit_ndx, current_perm, all_perms)
        # C: return the perms
        return all_perms
