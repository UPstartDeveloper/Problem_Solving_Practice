class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        """
        ints are unique
        is it guaranteed there will be a winner? - YES
        - YES: if the array is already sorted in reverse order
        - YES: if array is in sorted order, and 
        
        
        arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
              [1,11,22,33,44,55,66,77,88,99]
              [22,33,44,55,66,77,88,99, 1, 11]
        
        element. |  wins    
        11             1    
        22             1 
        33             1
        44             1   
        55             1
        
        {
            1: []
        }
        
        what happens is that the list goes into greatest to least order, and once that's the case
        we know we'll have a winner - that's the largest element
        
        will the winner always be the largest element:
        if k > number of spaces between the max and the 0 index
            - return the max element
        
        other wise:
        
           play the game, use a dict to know the winner
        """
        # find the max element, and it's index
        max_element = arr[0]
        max_index = 0
        for index, num in enumerate(arr):
            if num > max_element:
                max_element = num
                max_index = index
         # early exit
        if k > max_index - 0:
            return max_element
        # init a dict to map wins to elements
        nums_wins = dict()
        # while there is no winner:
        while k not in nums_wins.values():
            # get the elements at the 0 and 1 index
            elem1, elem2 = arr[0], arr[1]
            # give the larger one a win
            larger = 0
            if elem1 > elem2:
                larger = elem1
            else:
                larger = elem2
            if larger in nums_wins:
                nums_wins[larger] += 1
            else:
                nums_wins[larger] = 1
            # move the larger to index 0
            if larger == elem2:
                # swap first and second elements
                arr[0], arr[1] = arr[1], arr[0]
            # move the smaller to the end
            arr.append(arr.pop(1))
        # return the winner
        for num in nums_wins:
            if nums_wins[num] == k:
                return num