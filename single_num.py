"""
def find_max_power_of_2(max_num):
    exponent = 0
    power = 2**exponent
    while power <= max_num:
        exponent += 1
        power = 2**exponent
    return exponent + 1
  
def is_in_range(num, target_appearances, rest_appearances):
    x = 0
    range_value = target_appearances + rest_appearances*x
    while range_value < num:
        x += 1
        range_value = 3*x + 1
    return (range_value == num)

def align_nums(nums, bits_needed):
    for index, num in enumerate(nums):  # n iterations
        # see difference in lengthof num, and needed num of bits
        diff = bits_needed - len(num)  # O(1)
        # make up the length difference
        if diff > 0:
            # convert to list, to be able to insert
            num = list(num)
            # fill in 0's in front of num
            for position in range(diff):
                num.insert(0, '0')
            # convert back to string
            num = ''.join(num)
            # replace num in nums array
            nums[index] = num
    return nums
  

def single_number(nums):
    # find how long all the binary numbers need to be, n
    max_num = max(nums)  # O(n)
    bits_needed = find_max_power_of_2(max_num)  # O(n)
    # convert all the nums to their binary equivalents
    nums = [bin(num)[2:] for num in nums]  # O(n)
    # make sure all the nums are the same length
    nums = align_nums(nums, bits_needed)  
    print(nums)
    # create the final binary number we need to decode
    final_binary = list()
    # iterate over the range of (0, n)
    for bit_pos in range(bits_needed):
        # create a mask (1 << n)
        mask = 1 << bit_pos
        # count up the ones present in that bit pos, over all nums
        count = 0
        for num in nums:
            if (int(num, 2) & mask) > 0:
                count += 1
        # if that count is in the range of 3x + 1
        in_range = is_in_range(count, 1, 3)
        if in_range is True:
            # then add a 1 for that bit pos in final binary
            final_binary.append('1')
        else:  # count not in range of 3x + 1
            final_binary.append('0')
    # convert the bits into a string in right order
    final_binary.reverse()
    binary_str = ''.join(final_binary)
    # decode the binary number into base 10
    target_num = int(binary_str, 2) 
    return target_num

"""


# This model solution is from Prof. Narayan, at Cal State Monterey Bay

class Trinary:
    def __init__(self):
        self.bits = [0 for i in range(32)]
        print(f'Initialized Tri: {self.bits}')
    def xor(self, num):
        for i in range(32):
            bit = 1 << i
            if num & bit:
                print(f'Num: {num} and mask: {bit}')
                # when a bit occurs any multiple of three times, it will roll back to 0
                self.bits[i] = self.bits[i] + 1 if self.bits[i] + 1 <= 2 else 0
                print(f'Bits changed => {self.bits}')
    def value(self):
        num = 0
        for i in range(32):
            if self.bits[i] == 1:
                num |= 1 << i
        return num

def single_number(nums):
    tri = Trinary()
    for num in nums:
        tri.xor(num)
    return tri.value()
  


if __name__ == '__main__':
    nums = [3, 3, 3, 10]
    print(single_number(nums))
    