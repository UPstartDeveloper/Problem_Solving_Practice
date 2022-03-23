from collections import deque


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        """
        LeetCode: https://leetcode.com/problems/broken-calculator/
        
        inputs
            sV + t > 0
            sV < > t
            assue at least 1 way sV--> t
            
        Output:
            least # of ops sV --> t
            
        Intuition:
            d. prograiig
            directed graph theory
            
        EC: 
            sV == t ---> 0
            
        Approach:
        
            1) Brute force:
            
                init a binary tree
                BFS
                    dequeue a level of nodes
                    "visit" --> generate next level
                    l
                    enqueue(next_level)
                    
                    stop: find the target
                        return level_no - 1
                    
                    if no target:
                        level_no += 1
                        
            2)
        
        
        
        """
        ### HELPER
        pass
        
        ### DRIVER
        # EC:
        if startValue == target:
            return 0
        # abbreviations
        sV, t = startValue, target
        # A: init a binary tree
        level_no = 1
        q = deque([sV])
        # B: BFS
        while len(q) > 0:
            # dequeue a level of nodes
            level_size = len(q)
            # "visit" --> generate next level
            for _ in range(level_size):
                node = q.popleft()
                # find target?
                if node == target:
                    return level_no - 1
                else:  # enqueue(next_level)
                    q.append(node - 1)
                    q.append(node * 2)
            # if no target:
            level_no += 1
        # C: no path found?
        raise ValueError(f"Cannot fix calculator {sV} into {t}")
        
        
