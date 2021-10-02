def alternative_sort(nums):
    nums.sort(reverse=True)
    output, hi, low = list(), 0, len(nums) - 1
    while hi < low:
        output.extend([nums[hi], nums[low]])
        hi += 1
        low -= 1
    if hi == low and hi < len(nums):
        output.append(nums[hi])
    return output
