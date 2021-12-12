class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Leetcode: https://leetcode.com/problems/longest-common-subsequence/
        
        Input/Problem:
            2 non emmpty immutable string
            lowercase English
            longest subseque ----> common to both
        
        Output: len(longest_ss)
        
        Intuition:
            dynamic programming - globally optimal
        
        EC:
            - strings === ---> len(text1)
            - len(string) == 0 - N/A
            - text2 == reversed(text1)
                abs
                sba
            - TODO
            
        Approach:
        
            1) Brute force - 
                A: compute every subsequence of shorter str
                B: is_subsequence(other_text) ---> get longest
                
            2) Dynamic Programming
            
                let n = len(text1)
                let m = len(text2)
            
                dp_table = [
                
                         0       1        2         3        4        5
                         ''      a        b         c        d        e
                                 
                0   ''   0       0        0         0        0        0
                
                         
                1   a    0       1          
                
                
                2   c    0      
                
                
                3   e    0
                
                
                ]
                
                
                subproblem = cell
                to solve 1 subproblem:
                    if last letters === ----> 1 + (max(left, up, diagnonal))
                    if last letters !=  ----> (max(left, up, diagnonal))
                    
                O(n * m)
                
        """
        # 0: handle EC:
        if text1 == text2:
            return len(text1)
        elif text1 == '' or text2 == '':
            return 0
        # A: init dp_table
        table = [
            [0 for _ in range(len(text2) + 1)]
            for _ in range(len(text1) + 1)
        ]
        # B: solve subproblems
        for row_index in range(1, len(table)):
            for col_index in range(1, len(table[0])):
                char1, char2 = text1[row_index - 1], text2[col_index - 1]
                up, left, diagonal = (
                    table[row_index - 1][col_index],  # up
                    table[row_index][col_index - 1],  # left
                    table[row_index - 1][col_index - 1] # diagonal
                )
                # if last letters === ----> 1 + (max(left, up, diagnonal))
                if char1 == char2:
                    table[row_index][col_index] = diagonal + 1
                else: 
                    table[row_index][col_index] = max(up, diagonal, left)
        # C: return answer (from dp_table)
        return table[-1][-1]
