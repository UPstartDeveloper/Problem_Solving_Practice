"""
ITERATIVE SORTING ALGOS
"""


def bubble_sort(nums):
    pass


def insertion_sort(nums):
    """
    time: O(n^2)
    space: O(1)
    inplace/mutative
    iterative
    stable
    internal algorithm
    """
    # sort each index (after the first)
    for index in range(1, len(nums)):
        num_index, num = index, nums[index]
        # compare it backwards - find where it's sorted
        for prev_index in range(index - 1, -1, -1):
            prev_num = nums[prev_index]

            # "insertion"
            if prev_num > num:
                nums[prev_index] = num
                nums[num_index] = prev_num
                num_index = prev_index

    return nums


def selection_sort(nums):
    pass


"""
DIVIDE and CONQUER
"""


def merge_sort(nums):
    """
    time: O(n log(n))
    space: O(n)
    non-mutative/out-of-place
    recursive
    internal
    stable
    """
    ### HELPER
    def _merge(left, right):
        left_index = li = 0
        right_index = ri = 0
        merged = list()

        while li < len(left) and ri < len(right):
            if left[li] <= right[ri]:
                merged.append(left[li])
                li += 1
            else:
                merged.append(right[ri])
                ri += 1

        return merged

    ### DRIVER
    # base case: arr.length < 2
    if len(nums) < 2:
        return nums
    # recursive:
    mid = len(nums) // 2
    # sort the left
    sorted_l = merge_sort(nums[:mid])
    # sort the right
    sorted_r = merge_sort(nums[mid:])
    # merge!
    return _merge(sorted_l, sorted_r)


def quick_sort(nums):
    """
    O(n log n) - O(n^2) time, depending on the partitioning scheme and pivot
        - but usually tends toward linearithmic as n increases
    O(log n) - O(n) space
    in-place
    unstable
    internal
    recursive
    """

    def _partition(low, high):
        # choose the last element as the pivot
        pivot = high
        iterator, less_than_tail = low, low - 1

        while iterator < pivot:
            # if current elem < pivot, throw it "backwards" in the range
            if nums[iterator] < nums[pivot]:
                less_than_tail += 1
                nums[iterator], nums[less_than_tail] = (
                    nums[less_than_tail],
                    nums[iterator],
                )
            iterator += 1

        # move the pivot into place
        nums[pivot], nums[less_than_tail + 1] = (nums[less_than_tail + 1], nums[pivot])
        return less_than_tail + 1

    def _recursor(low, high):
        # base case: nothing to partition
        if low >= high:
            return
        # recursive: sort the pivot into place
        pivot = _partition(low, high)
        # recurse on left
        _recursor(low, pivot - 1)
        # recurse on right side
        _recursor(pivot + 1, high)
        return nums

    # init case
    return _recursor(0, len(nums) - 1)


if __name__ == "__main__":
    arr = [-7, 6, 3, 3, 1, 5, -8]
    print(quick_sort(arr))
