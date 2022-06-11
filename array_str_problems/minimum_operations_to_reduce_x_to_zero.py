class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        Input:
            nums: int[immutable, non-empty, unsorted, dupes, pos].len > 0
            X: int, pos
            
        Output:
            min(num_op)
            op - take 1 elem from left or right, decrease x
            
        Intuition:
            deque
            two pointers
            DP
            
        EC:
            x = 0 --> 0
            empty arr -> -1
            
        Approach:
        
            1) DIY - O(n), O(1)
                
                A: init sum_so_far = 0 (values we've used so far)
                    and num_ops = 0
                    
                B: two pters at both ends
                
                C: move the pters towards each other
                
                    choose the greater of the pointers (w/o making ssf > x)
                    if there is -> do an op:
                        increment ssf
                        increment num_ops
                        move that pter "inwards"
                    else if not:
                        stop
                    
                    other stop cond: pters cross
                    
                D: return num_ops if ssf == x, else 0
 
        """
        ### guard clauses
        if x == 0:
            return 0
        elif len(nums) == 0:
            return -1

        ### DRIVER
        sum_so_far = ssf = 0
        steps = 0

        index1 = p1 = 0
        index2 = p2 = len(nums) - 1

        while p1 <= p2:
            # get the largest of those THAT FIT
            elem1, elem2 = nums[p1], nums[p2]
            # if there is a way to update ssf -> do an op:
            # TODO[test] - what if elem1 == elem2, p1 != p2, and we want p2?
            ends = [elem1, elem2]
            candidates = sorted([e for e in ends if ssf + e <= x], reverse=True)

            # stop condition
            if len(candidates) == 0:
                break

            # keep going
            else:
                chosen = candidates[0]
                ssf += chosen
                steps += 1
                # move the appropiate pter
                if chosen == elem1:
                    p1 += 1
                else:
                    p2 -= 1

        return steps if ssf == x else -1
