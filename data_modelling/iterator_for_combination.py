class CombinationIterator:
    """
    Leetcode: https://leetcode.com/problems/iterator-for-combination/
    
    Input/Problem:
        string = n chars
        unique
        sorted
        immutable
        Define vars:
          let k = combinationanLength
          let n = len(characters)
          ASSUME 1 <= k <= n

    Problem - generate all the combos, sorted order
    
    Intuition:
       A: List[combinations] - recursive backtracking
       hasNext(): current_index < len(combinations) ---> T/F
       next: c[current_index]; current_index += 1
       
    Edge Cases:
        1) Invalid inputs - k = 0; characters == ""; dupes ---> ValueError
        2) TODO
        
    Approach: BELOW
    
    Complexity Analysis:
      Time: O(k * n!)
      Space: ---> this can be calculated using the formula for combinations,
                  since the space complexity is mainly determined by the 
                  space needed for the self.combos list.
                  Can say this is basically expressed as O(n! / k!)
        
    """

    def __init__(self, characters: str, combinationLength: int):
        self.size = combinationLength
        self.chars = characters
        self.combos = list()
        self._generate_combinations([], 0)
        self.current_index = 0
        
    def _generate_combinations(self, current_combo, choice_index):        
        ### DRIVER
        # Base Case: all done!
        if len(current_combo) == self.size:
            self.combos.append(''.join(current_combo))
        # Recursive Case: keep going
        else:
            for next_index in range(choice_index, len(self.chars)):
                char = self.chars[next_index]
                current_combo.append(char)
                self._generate_combinations(current_combo, next_index + 1)
                current_combo.pop()

    def next(self) -> str:
        next_combo = self.combos[self.current_index]
        self.current_index += 1
        return next_combo

    def hasNext(self) -> bool:
        return self.current_index < len(self.combos)
        

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

"""
chars = "abc"
self.size = 2

current_combo = ['a']

all_combos = []
            0.   1.   2
choices = ['a', 'b', 'c'] ------> ['b', 'c']
  index     ^
  next_index  ^
            
---------------------------------------

SF #2

current_combo = ['a'] ---- 

all_combos = []

choices = []'c']

"""
