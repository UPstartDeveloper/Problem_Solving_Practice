"""
array of ints 

unsorted
10^01 --> 11

11^01 = 10
[1,2,1,2,3] ==> 3
 0 1 3 2 0
 1 3 2 0 3


[1,1,2,2,3]
 0 1 0 2 0
 1 0 2 0 3

 [0, 0, 1] --> 1
 0   0

Intuition: find the unique elem in the array
Approach:
A: time O(n),  O(n)
- freq dist -- type: token
                1: 2,
                2: 2,
                3: 1
B: linear search to find the unique

Edge Cases:
- empty array --> None

XOR = ^
if diff --> 1

Identity Property of XOR w/ 0 - returns whatever the second operand is
0^0 --> 0
0^1 --> 1

"""

def find_unique(nums):
    unique = None
    # iterate over arr
    if len(nums) > 0:
        unique = 0
        for num in nums:
            # XOR
            unique ^= num
    return unique


if __name__ == "__main__":
    nums = [1,-2,1,-2,3]
    print(find_unique(nums))
