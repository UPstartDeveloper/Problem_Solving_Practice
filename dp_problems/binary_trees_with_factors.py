fromm typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """
        Leetcode: https://leetcode.com/problems/binary-trees-with-factors/
        
        Input/Problem:
            distinct, non empty, immutable, int[] > 1
            CANNOT ASSUME sorted
            leaf = any value
            parent = children are factors of parent.val
            
            insights:
            - order matters (except when children are same value)
            - trees have to be FULL (0 or 2 kids)
            - primary values (where 1 is its only other factor) have to be leaves
            
        Output:
            # permuations of binary trees
            output >= len(arr)
            
        Intuition:
            backtracking approach   
            recursion
            math
            
        EC:
            1) invalid input ---> ValueError
            
        Approach:
        
            1) Brute Force 
            2) Recursive Approach:
                A: total_count = sum(count from each value)
                   arr_set = set(arr)
                
                B: count_per_value = cpv = 1
                    for each pair of factors for that value:
                        # TODO: memoize these statements!
                        if factor1 == factor2
                            cpv += (count(factor1))
                        else if factor1 != factor1
                            cpv += (count(factor1) * count(factor2)) 
                            
                C: before for loop - make a dict of int --> set of tuple factors
                    for a given num:
                        factors, factor1 = set(), 2
                        while factor1 < pow(num, 0.5):
                            if num % factor1 == 0:
                                factor2 = num / factor1
                                pair = (factor1, factor2)
                                if factor1 in arr_set and factor2 in arr_set:
                                    factors.add(pair)
                            factor1 += 1
                        return factors                                
                
                D: Goal: return total_count
          
        Complexity: TODO
        
        """
        pass
 
