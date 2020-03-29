

'''
Idea #1
Brute force solution.

Questions:
Are repeat pairs allowed? ==> no
Are the numbers only positive integers?
How do we output the pairs found? list of lists

Pseudocode
needs the following:
1. iterate over each number in the array
2. for each number, iterate through all other numbers
3. on an single iteration, sum the number from the outer loop (num_1) and inner loop (num_2)
4. if their sums match, then output them together as a list
'''


def all_pairs_matching_sum(a, t):
    '''a is the array, t is the sum.
       Runtime Complexity: O(n^2), where n = len(a)
    '''
    num_1 = 0
    num_2 = 0
    matching_pairs = list()
    # iterate through numbers in the list
    for i in range(len(a)):
        num_1 = a[i]
        # iterate through all other numbers in a
        for j in range(len(a)):
            # do not compare a number to itself
            if not i == j:
                num_2 = a[j]
                # sum
                if num_1 + num_2 == t:
                    pair = [num_1, num_2]
                    duplicate_pair = [num_2, num_1]
                    if duplicate_pair not in matching_pairs:
                        matching_pairs.append(pair)
    return matching_pairs

'''
Given two arrays, determine if both arrays contain exactly the same elements
Input [1,2,5,4,0] and [4,2,5,0,1] -> Yes
Input [1,7,1] and [7,7,1]  No
'''


def compare_arrays(arr_1, arr_2):
    '''Compare using length of list, and distribution of list elements'''
    if not len(arr_1) == len(arr_2):
        return False
    # make histograms of both lists
    hist_1 = {}
    for num in arr_1:
        if num not in hist_1:
            hist_1[num] = 0
        else:
            hist_1[num] += 1
    hist_2 = {}
    for num in arr_2:
        if num not in hist_2:
            hist_2[num] = 0
        else:
            hist_2[num] += 1

    for key in hist_1.keys():
        if (key not in hist_2.keys()) or (not hist_1[key] == hist_2[key]):
            return False
    return True


if __name__ == '__main__':
    array_1 = [1, 2, 5, 4, 0]
    array_2 = [4, 2, 5, 0, 1]
    print(compare_arrays(array_1, array_2))

    array_1 = [1, 7, 1]
    array_2 = [7, 7, 1]
    print(compare_arrays(array_1, array_2))
