from typing import List


class Solution:
    def __init__(self):
        self.valid_schemes = 0
        self.schemes = set()
        
    def map_profits_groups(self, group: List[int], profit: List[int]) -> None:
        '''
        map the indicies of the profit array, to the corresponding profit and size
        
        e.g. 
        {
        0: (6, 2),
        1: (7, 3),
        2: (8, 5)
        }
        '''
        self.profit_groups = dict()
        # create the keys and values
        for crime_index in range(len(group)):
            profit_group = (profit[crime_index], group[crime_index])
            self.profit_groups[crime_index] = profit_group
        return None
    
    def scheme_valid(self, crimes: tuple[int], total_members: int, minProfit: int) -> bool:
        # init the is_valid
        is_valid = False
        # A: find the total profit and group members needed
        total_profit, group_size = 0, 0
        for index in crimes:
            profit, group_needed = self.profit_groups[index]
            total_profit += profit
            group_size += group_needed
        # B: return T/F 
        if total_profit >= minProfit and group_size <= total_members:
            is_valid = True
        # C: add to the list of already seen schemes
        self.schemes.add(crimes)
        return is_valid, total_profit, group_size
    
    def profitableSchemes(self, total_members: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """
        n people
        list of profits from crimes, another list of group size needed for it
        1 person can only participate in 1 crime 
        
        
        Question:
        - return number of possible ways the members can generate >= minProfit
        - order in which the crimes are committed doesn't matter
        - group and profit are always equal in length
        
        Testing Input:
        
        n = 10, 
        minProfit = 5, 
        
        group = [2,3,5], 
        
        profit = [6,7,8]
        
        1. crime 0 
        profit_so_far = 6, members_left = 8 
        
        Brainstorm:
        
        1. Backtracking
                                    people_left = n = 10, profit_so_far = 0, crimes = [], ca = [0, 1, 2]
                                    /                               |           ns = []
                                pl = 8, psf = 6, c = [0], ca [1, 2]       pl = 8, psf = 6, c = [1, ], ca = [0, 2]
                                /                                                   |
                            pl = 5, psf, 13, c = [0, 1]                     c = [1, 0], ca = [2]
                            /
                        pl = 0, psf = 22, c = [0, 1, 2] `
                                                
        Intution: backtrack through all possible combos of the crimes, return the number that are valid
        Approach: 
        # A: map the indicies of the profit array, to the corresponding profit and size
        # B: within the larger scope, keep track of valid_schemes
        # C: backtrack through all the combinations in the array
            # if scheme_valid() is True, we increment valid_schemes
        # D: return valid_schemes
        
        """
        def generate_schemes(current_scheme: tuple[int], crimes_available: List[int]):
            # A: check if the current scheme is valid, 
            is_valid, total_profit, group_size = (
                self.scheme_valid(current_scheme, total_members, minProfit)
            )
            if is_valid is True:
                self.valid_schemes += 1
            # B: try the next scheme, if there's room for more crime
            if group_size <= total_members:
                for index, next_crime in enumerate(crimes_available):
                    # make the next scheme
                    next_scheme = [crime for crime in current_scheme]
                    next_scheme.append(next_crime)
                    # update the list of crimes available
                    new_available_crimes = [
                        crime for crime in crimes_available if crime != next_crime
                    ]
                    next_scheme = tuple(sorted(next_scheme))
                    if next_scheme not in self.schemes:
                        generate_schemes(next_scheme, new_available_crimes)
            return None
        
        # A: map the indicies of the profit array, to the corresponding profit and size
        self.map_profits_groups(group, profit)  
        # B: init the crime scheme
        scheme, crimes_available = (
            (),
            [crime_index for crime_index in range(len(group))] # 3 --> [0, 1, 2]
        )
        # C: backtrack through all the combinations in the array
        generate_schemes(scheme, crimes_available)
        # D: return valid_schemes
        return self.valid_schemes % (10**9 + 7)

"""
Big O Analysis:
Time: O(g!g), where g is the length of the group (or profit) array
Space: same as for time, because we stored each unique combination
"""
