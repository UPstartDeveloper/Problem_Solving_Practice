from itertools import permutations

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        arithmic progress - all elements in arr are ordered so that the difference between
        any two contigiuous elemtns is the same throughtout 
        
         Clarifying
        - can we assume that there's always at least 1 element in the array? yes
        - does a 1 element count as an arithmetic progression? yes
        - are all the elements in the array unique? no
        - am I allowed to use the built-in permutations function? yes
        
        Insights: 
         for any array we've got, there's a set of the different permutations of that array
        and we basically want to choose a particular (or could be multiple ways to order it?) ordering
        
        
        Brute force - Idea #1
            1. try all possible orderings of the array, and see if one of them is an arithmethic 
                progression
                - not very efficient - exponential in time 
                - just to return False, we wouldn't know (it seems like), until we had tried all the 
                    permutations
        
        Pseucode:
            - generate all possible permutations - backtracking
                - then store in a list
            - then iterate over the list
                - decide if a perm is an arith-prog, and returrn True if so
            - return False
            
        now we have that set of possible permutations - we want to avoid having to calculate all of 
            them, because that's costly
        and the premise of this problem is to find how we could be ordered as an arith progr- so it 
        seems like a good case for dp!
            
        Idea #2 - dp
          [3] --> True
          [3, 5] --> True
          
          [3, 5, 1] --> False
          [3, 1, 5] --> False
          
          once we have seen one perm of the array that doesn't work, we can discount all others
          that start with the same element as that one
          
          [5, 3, 1] --> True
          
          - so maybe a faster way to get to the solution is to just swap out the first number with 
            another? (save the one's we've already tried in a list or something like that)
            
            
          [1, 2, 4] --> F, we see that this doesn't work        [1]
          
          [2, 1, 4]     F                                        [1, 2]
          [4, 2, 1]     F                                        [1, 2, 4] F
          
          
          [6, 6, 6, 6, 7]   F
          [7, 6, 6, 6, 6,]  F                                   [6, 7]
          
          Special Case for When the List Has Duplicates
            - if the list is not all one unique number, then it's False
            - we want to keep a set of the elements we've already tried in the first spot (also faster)
        
        
        """
        def is_arith_prog(array):
            '''Iterate over the array, make sure the difference between each element is the same.'''
            # get the diff between just the first two elements 
            # iterate for the rest of the array, and check if the difference between the next two 
            # elements is the same
            diff = array[1] - array[0]
            for index, num in enumerate(array[:-1]):  # first iteration is redundant
                print(index)
                num_after = array[index + 1]
                next_diff = num_after - num
                if next_diff != diff:
                    return False
            return True
        """
        '''Test out all the permutations'''
        if len(arr) <= 2:
            return True
        perms = list(permutations(arr))  # n!
        print(perms)
        for perm in perms:  # O(n * n!)
            if is_arith_prog(perm) is True:
                return True
        return False
        """
        """
        def reorder(array, next_first_elem_index, next_first_elem):
            # swap the current first element, with the next first element
            current_first = arr[0]
            arr[0], arr[next_first_elem_index] = next_first_elem, current_first
        # Early Exits
        # if arr has <= 2 elements --> T
        ARRAY_LENGTH = len(arr)
        if ARRAY_LENGTH <= 2:
            return True
        # store a set of the different elements in the array
        unique_elements = set(list(enumerate(arr)))
        # if the length of the set < length of the list --> F
        if ARRAY_LENGTH > len(unique_elements):
            return False
        # reorder the array initially
        first_elem_index, first_elem = unique_elements.pop()
        set_length = len(unique_elements)
        reorder(arr, first_elem_index, first_elem)
        # iterate while the set still contains number - possible numbers to put at the front
        while set_length > 0:
            if is_arith_prog(arr) is True:
                return True
            else:  # one permutation failed
                # remove the first elements from the set
                # unique_elements.remove((first_elem_index, first_elem))
                # find the next element to put at the front
                next_front_elem_index, next_front_elem = unique_elements.pop()
                # print(unique_elements)
                # reorder the arr
                reorder(arr, next_front_elem_index, next_front_elem)
                print(arr, unique_elements)
                # decrement set_length
                set_length -= 1
        return False
        """
        sorted_array = sorted(arr)
        print(sorted_array)
        reverse_sorted_array = sorted(arr, reverse=True)
        print(reverse_sorted_array)
        return (is_arith_prog(sorted_array) or is_arith_prog(reverse_sorted_array))
                