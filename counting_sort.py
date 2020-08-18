def color_sort(nums):
    """Implements the Counting Sort algorithm.
       
       :type nums: List[int]
       :rtype: None
    
    """
    # populate an array of the counts of each color
    counts = [0 for _ in range(3)]
    for color in nums:
        counts[color] += 1
    # reassign the appropiate color into each index in nums
    index = 0
    for color, count in enumerate(counts):
        for _ in range(count):
            nums[index] = color  # total of n iterations
            index += 1
    return None


if __name__ == '__main__':
    nums = [0, 1, 0, 1, 2, 1]
    color_sort(nums)
    print(nums)  # --> [0, 0, 1, 1, 1, 2]
    
"""
Variable Table

counts = [2, 3, 1]

nums = [0, 0, 1, 1, 1, 2]

index = 5

color = 2, count = 1

"""