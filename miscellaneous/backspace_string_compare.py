class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        LeetCode: https://leetcode.com/problems/backspace-string-compare/
        
        Input/Problem:
            two non empty str
            repr std in streamms
            process what the editor recieves, commpare
            case insensitive 
            <---- #, not after 
        
        Approaches:
        
            1) Stack: lienar time and space O(s + t)
                A: make two stacks ----> for parsing
                B: parse both:
                    (letter --> stack.push())
                    ('#' ---> stack.pop() )
                C: return parsed_s == parsed_t 
                
            a##c
               ^
            [c] ---> parsed_s = 'c'
            
            #a#c
               ^
            [c] -----> parsed_t = 'c'

            2) In-place:
                TODO
                in-place means -----> 
                    only local variables OR use the call stack
                    
                    Recursive Approach:
                        how do I k
                        
                    ab#c
                    
                    ad#c
                     ^
                     
            3) Fail Fast:
                start from end
                if both are chars AND == ----> move both back 
                if both chars and != ---> False
                if one pointer == #
                    count up how many # in a row 
                    mv the pointer back by 2 * #_count
                if reach the end of one but not the other
                    ----> check if the unfinished is just leading # ---> return T/F based on the case
                if reach the end of both at the same time and no errors ---> True
                
        EC: TODO: think 
            - multiple pounds in a row
            - invalid strs
            - s and t == -----> auto-True
        """

        def _parse(string):
            stack = list()
            for char in string:
                if char.isalpha():
                    stack.append(char)
                elif len(stack) > 0:
                    stack.pop()
            return "".join(stack)

        return _parse(s) == _parse(t)
