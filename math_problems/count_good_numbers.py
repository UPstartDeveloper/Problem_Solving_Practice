class Solution:
    def __init__(self):
        self.DIVISOR = (10 ** 9) + 7

    def countGoodNumbers(self, n: int) -> int:
        """
        Leetcode: https://leetcode.com/problems/count-good-numbers/
        
        Input/Problem:
            n - pos int
            count # poss good digit str
            digit str:
                - can leading 0's
                - can have dupes
        
        Output:
            - return total_count % (10**9 + 7)
            
        Intuition:
            permutations
            recursion
            
        EC:
            - n is outside the range ---> ValueError
            
        Approach ---> O(1) time and space
            The solution can be derived from the formula (the intuition comes from making a call tree):
                total_count = 1 * (5 ** x) * (4 ** y)
                
            where:
                x = n // 2 (b/c we alt multiplying by 5 and 4, it might be one higher if n is odd)
                y = n // 2 
                
            then we just need to make sure we are always doing modulo division
        """
        half = n // 2
        first_term = pow(5, (half + (n % 2)), self.DIVISOR)
        second_term = pow(4, half, self.DIVISOR)
        return (first_term * second_term) % self.DIVISOR
