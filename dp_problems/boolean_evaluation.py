from collections import Counter, defaultdict


class Solution:

    CHAR_SET = {"|", "&", "^", "1", "0"}

    def count_eval(self, expression: str, result: bool) -> int:
        """
        Cracking the Coding Interview 8.14
        Boolean Evaluation: 
            Given a boolean expression consisting of the symbols:
                0 (false), 
                1 (true),
                & (AND), 
                | (OR), and 
                ^ (XOR), 
            and a desired boolean result value result, 
            implement a function to count the number of ways of 
            parenthesizing the expression such that it evaluates to result.

        EXAMPLE 1
        countEval("1 ^ 0 | 0 | 1", false) -> 2 
        EXAMPLE 2
        countEval("0 & 0 & 0 & 1 ^ 1 | 0", true) -> 10
        """
        ### HELPERS
        def _validate_str(expression):
            # invalid chars
            histogram = Counter(expression)
            if histogram.keys != self.CHAR_SET:
                raise ValueError(f"The expression {expression} has disallowed chars.")
            # bits that are longer than they should be
            for idx, char in enumerate(list(expression)):
                if char in {"&", "|", "^"}:
                    if (
                        not (0 < idx < len(expression) - 1) or
                        not expression[idx - 1].isnumeric() or 
                        not expression[idx + 1].isnumeric()
                    ):
                        raise ValueError(f"The expression {expression} has malformed operators.")
                elif char in {"0", "1"}:
                    if (
                        (idx < len(expression) - 1 and expression[idx + 1].isnumeric()) 
                         or 
                        (idx > 0 and expression[idx - 1].isnumeric()) 
                    ):
                        raise ValueError(f"The expression {expression} has malformed operands.")

        ### DRIVER
        # A: check for edge cases
        if len(expression) == 0:
            return 0  # empty str
        _validate_str(expression)
        # B: TODO: assign labels to each operator
        ...
        # C: TODO: generate all possible orders of operation

        # D: TODO: double-check which actually equal the result

        # E: TODO: return the count
        pass