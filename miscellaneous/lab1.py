"""
Given a sorted array,
find the index of the first and last occurrence
of a given element.
If the given element is not found in the array, report that.

- integers
- return a tuple
- "Not found"


[ -9, -5, -5, 0, 4, 6], -5 => (1, 2)

1. create a histogram of the values in the array - O(n)
- histo = {}
- map the array elements to their [] of their indices

2. iterate over the items in histogram


"""

"""
Array a of numbers
target t

sorted array
find a pair of numbers in array a that sum to t

return the elements in a that sum to t => [a, b] =

just integers, positives and negatives
if cannot be found return empty lists

a =
[-3, -2, -1, 0, 1, 2, 3]

t = -3

[0, 3]
1. iterate through all the list elements
    - keep track of i, index position I'm currently

    2. on each iteration find the possible sums
    3. if found, return values in a values


trade-off
-slow
- not account for duplicates
"""


def two_sum(array, target):
    for i in range(len(array)):
        addend_1 = array[i]
        for j in range(i + 1, len(array)):
            addend_2 = array[j]
            if target == addend_1 + addend_2:
                return [addend_1, addend_2]


if __name__ == "__main__":
    print(two_sum([-3, -2, -1, 0, 1, 2, 3], -3))
