class Solution:
    def count_vowel_strings(self, n: int) -> int:
        """
        LeetCode: https://leetcode.com/problems/count-sorted-vowel-strings/
        
        Input: 
            pos int < 51
        
        Output:
            int
            
        Intuition:
            permutations
                limiited to only vowels
                has to be sorted (L -> G)
                BUT we can have duplicates
                
                tree data structurre
                    each node has 5 kids
                    depth of the tree = n
                    
                each root -> leaf path ---> 1 valid string
                
        Edge Cases:
            n <= 0 or n > 50 --> ValueError?
            
        Approach:
        
        1) Tree approach:
        
            A: build the char tree - 5-way, n levels
            B: backtrack to find all the root --> leaf paths ---> O(n * 5^n)
                a) if it's lexico-sorted - count it toward output
            C: return the count
            
        2) Slimmed-down tree approach --> O(5^n)
            - valid chars, correct number, and already sorted order
            A: like 1)
            B: like 1), but letter can only have children letters => to itself
            C: like 1) 
            
        3) math approach: BELOW
            
            goal: find number of branches that "lead" into root leaves
            Time: O(string_length)
            Space: O(1)
            
               
        """        
        ### DRIVER
        # A: guard clause
        if n < 1 or n > 50:
            raise ValueError(f"n has to be between 1 and 50, inclusive.")
        # B: define initial distribution of a's, e's, i's, and so forth
        num_vowels = 5
        dist = [1 for _ in range(num_vowels)]  # let's say this is for level 1
        # C: update array w/ new distribution of vowels in each level afterward
        for level_number in range(2, 2 + (n - 1)):
            prefix_sum = 0
            for index in range(len(dist)):
                # "swap" out the number of this char's appearances, for that in the current level
                last_count = dist[index]
                prefix_sum += last_count
                dist[index] = prefix_sum
        # D: return the total number of sorted strings in the last level
        return sum(dist)
    
    
    # TEST CASES
    
    # n = 0  ✅
    
    # n = 1
    # count = 0, 1, 2, 3, 4, 5 
    # choices = [1, 2, 3, 4, 5]
    # letter.          ^
    # current_perm = [ ]
    # last_added = 0
    
    
    # n = 2  ✅
    
    
    # n = 33 --> ✅
