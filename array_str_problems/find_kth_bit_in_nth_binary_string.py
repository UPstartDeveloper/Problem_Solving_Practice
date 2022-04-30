class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        LeetCode: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
        
        Input/Problem:
            2 ints pos, immutable
            S = recursive
            binary str
            
        Output:
            k = index
            S_n[k]
            
        Intuition:
            recursive
        
        EC:
            - n/k not pos ---> ValueError
            - TODO
            
        Approach:
        
            1. DIY:
                A: form S_n
                i     0.   1.   2.   n-1
                    [S_1, S_2, ...   S_n]
                B: concat all S_i's --> S_n_all[k]
                
        Time: O(n * (2^n))
        Space: O(2^n)
        """
        ### HELPERS
        def _modify(prev_str):
            inverted = "".join(["1" if char == "0" else "0" for char in list(prev_str)])
            return inverted[::-1]

        ### MAIN
        # A: form S_n
        last_str = "0"
        for index in range(1, n):  # n iterations
            last_str = "".join([last_str, str(1), _modify(last_str)])  # O(2 * 2^n)
        # B: return kth bit
        return last_str[k - 1]
