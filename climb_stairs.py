import math

class Solution(object):
    def __init__(self): 
        self.num_paths_overall = 0
        self.distance_so_far = 0
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        
        n = number of steps to climb
        1's, 2's, 1's and 2's 
        
        Return the number of ways to climb (permutations)
        
        High level thinking:
        
        Idea #1: get all the permuations of 1 or/and 2 that add up to n
        
        Insights:
        return value: num_paths
        always at least 1 path to the top
        if n is even, add 1 more path to the return value right away
        
        # Overall: how many ways can I get to the top? (travel n steps)
            for one of the ways: 
            
            # sub-question: how many steps will this way to the top take?
            - just use steps of size 1 - always applicable
            - just use steps of size 2 - even only
            - just use of steps of (1 + 2) = 3 - may not always be applicable
        
            # how many steps will I take overall?
            steps of sizes and 1 and 2, availble steps is passed into the function
            how many steps of 1 do I take?
            how many 2 do I take?
            what's the ordering of the 1's and 2's?
                1x + 2y = n
                x + y = available_steps
                num_paths += 1
                
                           [_, _, _, _, _, _, _]
                            /\
                          1, 
                         /
                        1, 1
                       /
                     1, 1, 1,
                    /
                1,1,1,1,1,1,1,1
            value n = 10
            1 1 1 1 1 1 1 1 1 1 
            2 1,1,1,1,1,1,1
            1,1,1,1,2,1,1,1,1
            2.2,2,1,1,2,
            
            HELPER
            init AS [1,1,0,0,0,0,0]     [1,2,0,0,0,0,0]
                    [2, 1,0,0,0,0,0]                                    [2, 2,0,0,0,0,0]              
            find_steps(list of AS, n, index):
                Q: do I still need to put in more steps?
                Base
                if yes:
                    calculate the sum of AS
                    if it == n, increment count (for this AS)
                    if it != n, do nothing
                else:
                    put in another 1, call the func again
                    put in another 2, call the func again
                
                
            
            
            _ _ _ _ _ _ _ _ _ _
            paths = 1, 2, 3, 4, 5, 6, 10, 14, 18
            
        # Ways to Generate Paths
        1. Start with a path of all 1's
        2. 
        
        
        Repeated: 
        1. replacing two 1's, with one 2
        
        How would we know when to stop?
        
        max_ones = n  --> upper bound
        max_twos = if n is even, then n / 2 is another path  --> lower bound
                n = 1
                1 1 1 1 1 1 1 1 1 1 
                
        iterate over range of all possible num_Steps:
            find out all the permutations of 1 and 2's, for this number of steps
                - let's say the number available steps is 7
                - we want to travel 10 steps, using 1's and 2's
                    _ _ _ _ _ _ _ 
                    1 , 2, 1, 2, 2, 1 ,1
                    
            add that number to the number of paths overalll
                

        # Idea 2:
        
        init a sum_so_far
        
            []
            
            
        find_steps(list of AS, n, index):
                Q: do I still need to put in more steps?
                Base
                if yes:
                    calculate the sum of AS
                    if it == n, increment count (for this AS)
                    if it != n, do nothing
                else:
                    put in another 1, call the func again
                    put in another 2, call the func again
        
        """
        """
        # --------------------------------------------------------
        def calculate_upper_lower():
            lower_bound = 0
            # calculate lower bound
            if n % 3 == 0:
                lower_bound = n / 3
            elif n % 2 == 0:
                lower_bound = n / 2
            else: 
                lower_bound = int(n / 2) + (n % 2)
            return n, lower_bound
        # --------------------------------------------------------
        # --------------------------------------------------------
        def calculate_paths(available_steps):
            # init the num_paths for given step
            # num_paths_given_available_steps = 0
            # allocate memory for the empty list
            # global num_paths_overall
            path = [0 for _ in range(available_steps)]
            # init index
            index = 0
            # [0,0,0,0,0,0,0,0,0]
            # ------------------------------------------------
            def find_steps(path, index, next_number_to_add=None):
                if next_number_to_add is not None:
                    path[index] = next_number_to_add
                    index += 1
                # do I still need to put in more steps?
                if index == len(path):
                    # calculate the sum of path
                    distance_travelled = sum(path)
                    if distance_travelled == n:
                        self.num_paths_overall += 1
                else:  # index < path
                    # put in another 1, call the func again
                    find_steps(path, index, next_number_to_add=1)
                    # put in another 2, call the func again
                    find_steps(path, index, next_number_to_add=2) 
            # -------------------------------------------------
            # num_paths_given_available_steps = find_steps(path, index)
            find_steps(path, index)
            # return num_paths_given_available_steps 
            return 
        # calculate the upper bound for available steps
        # calculate the lower bound for available steps
        upper_bound, lower_bound = calculate_upper_lower()
        # iterate of available steps    (n - n/2 = n /2 ) - linear
        for available_steps in range(lower_bound, upper_bound + 1):
            # calculate all the perms of steps under those constraints (available steps, n)
            # num_paths_for_given_steps = calculate_paths(available_steps)
            calculate_paths(available_steps)
            # increment the total number of path, by this value
            # num_paths_overall += num_paths_for_given_steps
        # return the total paths
        return self.num_paths_overall
        """
        dist_so_far = 0
        paths_found = set()
        def calculate_paths(dist_so_far, additional_dist):
            # otherwise find out if this led to the n
            if (dist_so_far + additional_dist) == n:
                self.num_paths_overall += 1
                paths_found.add((dist_so_far, additional_dist))
                return
            # or add more steps if need be
            elif dist_so_far < n:
                # check if this stack frame is already known to lead to n:
                if (dist_so_far, additional_dist) in paths_found:
                    # then increment and return earlier
                    self.num_paths_overall += 1
                # otherwise travel down the recursion tree
                else:
                    dist_so_far += additional_dist
                    calculate_paths(dist_so_far, 1)
                    calculate_paths(dist_so_far, 2)
            return
        calculate_paths(dist_so_far, 0)
        return self.num_paths_overall
        
    
    
"""
n = 10
num_paths_overall = 1 

upper_bound = 10
lower_bound = 5


---------------------------
available_steps = 5

num_paths_for_given_steps = __

num_paths_given_available_steps = 0
---------------------------------------------
path = [1,1,0,0,0]          index = 2      next_number_to_add=1

path = [1,1,0,0,0]          index = 2      next_number_to_add=1
----------------------------------------------------------------
       [1,0,0,0,0]                  1       
path = [0,0,0,0,0]          index = 0       next_number_to_add=1
-----------------------------------------------
path = [0,0,0,0,0]          index = 0


1, 2, 1, 2,
_ _ _ _ _

1, 1, 1, 1, 1


5!
______ =========> 20
(5 - 2)!



n = 2

lower = 1
upper = 2

available_steps = 1

path = [0]
index = 0


value of n

path_so_far = 0
num_paths

base case: 
psf == n
    increment num_paths

increment psf by 1, again
increment psf by 2, call again
"""
