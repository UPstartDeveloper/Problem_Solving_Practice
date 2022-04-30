from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        LeetCode: https://leetcode.com/problems/validate-stack-sequences/
        
        Input:
            two int []
                non neg val
                non empty
                distinct
                not-sorted
                
        Output:
            bool --> validate some seq of push/pop ops
            
        Intuition:
            use a third stack
            
        EC:
            invalid input: popped != perm(pushed) --> ValueError
            
        Approach:
            
            A: init a validator stack
                1: pushed arr: push elems up till the first popped
                2: save pushed_ndx
            B: validate the seq
                1: init popped_ndx
                2: for each popped elem:
                    a) check if popped == top(validator)
                        if so --> validator.pop()
                        
                    OR
                    
                    b) if popped == pushed[pushed_ndx]
                        if so --> pushed_ndx += 1
                        
                    in a) or b) ---> popped_ndx += 1
                    
                    c) otherwise ---> False
            C: final check
                if pushed_ndx finised AND validator.is_empty() -> T/F
                
                    
        """
        ### MAIN
        # A: init a validator stack
        stack = []
        # B: validate the seq
        popped_ndx = 0
        for pushed_elem in pushed:
            # elems have to be pushed in sequential order
            stack.append(pushed_elem)
            # if we've pushed an elem -> then pop it before pushing any others
            while (
                # avoid index errors
                popped_ndx < len(popped)
                and len(stack) > 0
                and stack[-1] == popped[popped_ndx]
            ):
                stack.pop()
                popped_ndx += 1
        # C: final check
        return popped_ndx == len(popped)
