"""
Given a sorted array, find the index of the first and last
occurrence of a given element. If the given element is not found in the array, report that.

- integers, duplicates are allowed

element = 2
[2, 5, 6, 2]

output - [0, 3]

0: 2  --> 0, last_index = first_index + (number of occurences - 1)

Pseudocode
dict to map allow the value to its indices
index into the first and last

distribution =
{
  0: 1
  1: 1
}


index 1
num   2
"""


def find_indices(array, element):
    distribution = {}
    for index, num in enumerate(array):
        if num == element and (len(distribution.keys()) == 0):
            distribution[index] = 1
        elif num == element:
            for index in distribution.keys():
                distribution[index] += 1

    if len(distribution.keys()) == 1:
        for index in distribution.keys():
            return [index, index + (distribution[index] - 1)]
    else:
        return "Element not in list."


if __name__ == "__main__":
    print(find_indices([2, 2, 5, 6], 2))
