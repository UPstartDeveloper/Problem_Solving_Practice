class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = dict()

    def __call__(self, str1, str2):
        if (str1, str2) not in self.cache and (str2, str1) not in self.cache:
            self.cache[(str1, str2)] = self.func(str1, str2)
        answer = self.cache[(str1, str2)]
        return answer


@Memoize
def deletion_distance(str1, str2):
    # base cases:
    if str1 == str2:
        return 0
    elif str1 == "":
        return len(str2)
    elif str2 == "":
        return len(str1)
    # recursive cases: not totally equal
    elif str1[-1] != str2[-1]:
        # calculate the two possible deletion distances
        return 1 + min(
            deletion_distance(str1[:-1], str2), deletion_distance(str1, str2[:-1])
        )
    elif str1[-1] == str2[-1]:
        return deletion_distance(str1[:-1], str2[:-1])


"""
Deletion Distance

The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
Constraints:

[input] string str1
[input] string str2
[output] integer

"""


if __name__ == "__main__":
    # str1 = "some"
    # str2 = "thing"
    str1 = "ddddddddddddddddddddddddddddddddddddddddddddddddddddd"
    str2 = "fffffffffffffffffffffffffffffffffffffffffffffffffffff"
    print(deletion_distance(str1, str2))
