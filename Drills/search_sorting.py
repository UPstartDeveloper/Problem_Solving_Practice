from typing import List

def binary_search(nums: List[int], target: int, use_iterative=True) -> int:
    """Returns the index of the target elem in nums, or -1 if not found."""
    ### HELPERS
    def _bs_iterative():
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            found = nums[mid]
            if target < found:
                hi = mid - 1
            elif target > found:
                lo = mid + 1
            elif target == found:
                return mid
        # not found
        return -1

    def _bs_recursive(low=0, hi=len(nums)-1):
        mid = (low + hi) // 2
        found = nums[mid]
        # base cases
        if found == target:
            return mid
        elif low > hi:
            return -1
        # recursive cases
        elif target < found:
            return _bs_recursive(low, mid-1)
        elif target > found:
            return _bs_recursive(mid+1, hi)

    ### MAIN
    if use_iterative:
        return _bs_iterative()
    return _bs_recursive()


def bubble_sort(nums: List[int]) -> List[int]:
    """Bubble sort is a common sorting algo. It is:
    - O(n^2) time
    - O(1) space
    - mutative (aka done in place)
    - iterative
    - internal
    - stable

    """
    is_sorted = False
    # sort the array
    while is_sorted is False:
        swaps, ndx = 0, 0
        # pass over array
        while ndx < len(nums) - 1:
            ndx2 = ndx + 1
            elem1, elem2 = nums[ndx], nums[ndx2]
            # swap
            if elem1 > elem2:
                nums[ndx], nums[ndx2] = elem2, elem1
                swaps += 1
            # keep moving
            ndx += 1
        # another pass
        if swaps == 0:
            is_sorted = True
    # all done!
    return nums


def merge_sort(nums: List[int]) -> List[int]:
    """Merge sort is a common sorting algo. It is:
    - O(n * log(n)) time
    - O(n) space
    - mutative (aka done in place)
    - recrusive
    - internal
    - stable

    """
    ### HELPERS
    def _merge(left, right):
        merged = list()
        lndx = left_ndx = 0
        rndx = right_ndx = 0
        while lndx < len(left) and rndx < len(right):
            lefty, righty = left[lndx], right[rndx]
            merged.append(min(lefty, righty))
            if lefty <= righty:
                lndx += 1
            elif lefty > righty:
                rndx += 1
        # add remaining
        if lndx < len(left):
            merged.extend(left[lndx:])
        else:
            merged.extend(right[rndx:])
        return merged

    ### MAIN
    # Base Case
    if len(nums) < 2:
        return nums
    # Recursive 
    else:  # len(nums) >= 2:
        # divide
        mid = len(nums) // 2
        sorted_left, sorted_right = (
            merge_sort(nums[:mid]),
            merge_sort(nums[mid:])
        )
        # conquer
        return _merge(sorted_left, sorted_right)
