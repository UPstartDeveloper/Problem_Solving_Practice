def merge_sort(nums):
    '''Stable out of place algorithm for sorting, using divide and conquer.'''
    def merge_lists(list1, list2):
        """Merge two sorted lists into one larger sorted list
        This function helps in the CONQUER step
        """
        # have 2 indices for elements in list1 and list2
        index1, index2 = 0, 0
        # init list for all elements
        merged = list()
        # useful constants
        LENGTH1, LENGTH2 = len(list1), len(list2)
        # populate the merged list
        while index1 < LENGTH1 and index2 < LENGTH2:
            # get items from list1 and list2
            item1, item2 = list1[index1], list2[index2]
            # choose which one goes in the list
            if item1 <= item2:
                merged.append(item1)
                index1 += 1
            else:  # item1 > item2
                merged.append(item2)
                index2 += 1
        # merge any unmerged items
        if index1 < LENGTH1:
            merged.extend(list1[index1:])
        if index2 < LENGTH2:
            merged.extend(list2[index2:])
        return merged
    # Base Case
    if len(nums) == 1:
        return nums
    # DIVIDE - Recursive Case
    mid_index = len(nums) // 2
    # A: sort the left side
    left_subproblem = merge_sort(nums[:mid_index])
    # B: sort the right side
    right_subproblem = merge_sort(nums[mid_index:])
    print(f'Left:{left_subproblem}, and Right: {right_subproblem}')
    # CONQUER
    # C: sort them both into one larger sorted list
    merged = merge_lists(left_subproblem, right_subproblem)
    print(f'Just merged: {merged}')
    # E: place that list back into the input list
    return merged 
  
if __name__ == '__main__':
    nums = [2, 2,2,2,2,2,22,2,2,2,2, 6, 3,3, 1,2,2,2,2,22,2,2]
    print(merge_sort(nums))