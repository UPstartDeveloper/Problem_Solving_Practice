"""
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

{
1: 3,
2:2,
3: 1
}

[1, 2, 3]
 
 0  1  2  
[1  1  1]

find the index where to keep track of the count
index = max - (max) % val

sorting l -> h
index = val - min

[1, 2, 3]

[
  (1, 3),
  (2, 2),
  (3, 4)
],
k = 2

[
  (1, 3),
  (2, 2),
  (3, 4),
]

sortng it all - slow as n gets huge



sort - integer (CS, BS) - O(n)

Idea #1 - sorting the counts, maps back to the types

# make a frequency distrbution - dictionary - O(n)
  # type -> count
# dump key-value pairs into another list - O(n)
# sort by the counts, reverse (Desc order) - O(nlogn)
# make an empty list - k
  # keeping adding types until we hit k

O(k + (n log(n)))
Space - k + n


Idea #2 - avoid sorting all of the numbers
# make a frequency distrbution - dict - O(n)
  # type -> count
# dump key-value pairs into another list - O(n)
# init a list size k - output - O(k)
# preload the first k pairs O(k)
# iterate over rest of the pairs. n 
  # if a pair_count > smallest pair count, replace - constant
  # sort the output list - keep a pointer at where the smallest count is - k log k

# return the types of numbers

time - O(n* klogk)

k < n
k log k < n log n

Idea #3 - more space, less time
# make a frequency distrbution - dict - O(n)
  # type -> count
# dump key-value pairs into another list - O(n)
# sort the pairs by the counts - counting sort
#     - linear time and space - n + range(count)
# return the types of the largest k counts

O(k + n + range)
O(n)

Idea #4 - priority queue - 
--------------------------------------


counts - types
{
  1: [2, 1]
  2: [1, 2]
  3:
}

types - counts

"""
# Open prompt.md for coding challenge.


def top_n_frequent(nums, k):

    """ "
    # make a frequency distrbution - dictionary
    count_types = dict()
    # multiple passes
    for val in nums:
      count = 0
      for num in nums:
        if val == num:
          count += 1
      if count not in count_types:
        count_types[count] = [val]
      else:
        count_types[count].append(val)


    # dump key-value pairs into another list
    # sort by the counts, reverse (Desc order)
    # make an empty list
    # keeping adding types until we hit k
    """

    def is_first_k_filled(sp, k) -> bool:
        for index_sp in range(k):
            if sp[index_sp] == (0, 0):
                return False
        return True

    def make_distribution(nums):
        type_counts = dict()
        for num in nums:
            if num in type_counts:
                type_counts[num] += 1
            else:  # first time we've seen it
                type_counts[num] = 1
        return type_counts

    def sort(pairs):
        """sort by the count, least to greatest"""
        # counts = list()
        # find the lowest count
        min_count = float("inf")
        for index, pair in enumerate(pairs):
            key, value = pair
            if value < min_count:
                min_count = value
        # find the highest count
        max_count = 0
        for index, pair in enumerate(pairs):
            key, value = pair
            if value > max_count:
                max_count = value
        # allocate mem for the counts array
        sorted_pairs = [(0, 0) for _ in range(max_count - min_count + 1)]
        # find the counts of each count
        output = []
        # sorted_pairs = 0
        index = 0
        while not is_first_k_filled(sorted_pairs, k):
            pair = pairs[index]
            key, value = pair
            if value == max_count:
                index_sp = 0
            else:
                index_sp = max_count - (value % max_count)
            sorted_pairs[index_sp] = pair
            index += 1
        return [key for key, value in sorted_pairs[:k]]

    # make a frequency distrbution
    type_counts = make_distribution(nums)
    # dump key-value pairs into another list
    type_counts = list(type_counts.items())
    # sort the pairs by the counts
    output = sort(type_counts)
    # return the types of the largest k counts
    return output


"""print(3 - (1 % 3))
print(3 - (2 % 3))
print((3 % 3))"""

"""
nums = [1,1,1,2,2,3],
       [3, 2, 2, 1,1,1]
k = 2

tc = [
  (3, 1),
  (2, 2),
  (1, 3),
]

minc = 1
maxc = 3

sp = [
  0 
  (2, 2), 
  (3, 1)
]

o = [3, 2]

index = 1

pair = (2, 2)
k = 2
v = 2
isp = 1

3 - 

"""

nums = [1, 1, 1, 2, 2, 3]
k = 2
# print(top_k_frequent(nums, k))

"""
Idea #4 - heap

# make freq dist
# make a list of the kv pairs
# put the first k into a heapq (min heap)
# iterate over the rest - n - k
  # if new pair has count > min count
    # remove current min count
    # push the new pair into the heap
# take out the types in the heap as list

time = n log(k)
space = k for the heapq, n 
"""
from heapq import heappush, heappop, heappushpop


def top_k_frequent(nums, k):
    def make_distribution(nums):
        type_counts = dict()
        for num in nums:
            if num in type_counts:
                type_counts[num] += 1
            else:  # first time we've seen it
                type_counts[num] = 1
        return type_counts

    # make a frequency distrbution
    type_counts = make_distribution(nums)
    # make a list of the kv pairs
    type_counts = list(type_counts.items())
    # reverse the pairs
    for index, pair in enumerate(type_counts):
        type_counts[index] = (pair[1], pair[0])

    # put the first k into a heapq (min heap)
    heap = list()
    for index in range(k):
        pair = type_counts[index]
        heappush(heap, pair)
    # iterate over the rest - n - k
    for index in range(k, len(type_counts)):
        next_pair = type_counts[index]
        next_count, next_type = next_pair
        # if new pair has count > min count
        min_count, min_type = heap[0]
        if next_count > min_count:
            # remove current min count
            # push the new pair into the heap
            heappushpop(heap, next_pair)
    # take out the types in the heap as list
    output = list()
    for _ in range(k):
        pair = heappop(heap)
        count, type = pair
        output.append(type)
    return sorted(output)


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))
