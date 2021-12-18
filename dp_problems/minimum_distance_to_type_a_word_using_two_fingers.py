class Solution:
    def minimumDistance(self, word: str) -> int:
        """
        Leetcode: https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/
        
        Input/Problem:
            - 5 x 6 grid of all letters (last is only 2)
            - need to type out a word (input is immutable, order matters)
            -word is NOT empty
            - 2 fingers
                - first letter a finger goes to - 0 cost
            - distance = abs(x1 - x2) + abs(y1 - y2)
            
        Output:
            - dist w/ lowest distance for fingers
                total_dist = sum(dist travelled by both fingers)
            
        Intuition:
            - DP
            - recursion, or 
            - heaps
            
        Stepping Stone:
            - 1 finger ---> sum(dist between each letter)
            - 2 finger, greedy solution:
                a) for each next letter to type - cheaper to use f1 or f2?
            - 2 finger, optimal(?) ---> time is O(2^n)
                a) for each next letter to type - 
                recurse on using both f1 or f2 to type it (but no repeats)
                    b) figure out all the total distances that result 
                c) return all th distances found
                d) take the min of all the possible total_distances
        """
        pass
