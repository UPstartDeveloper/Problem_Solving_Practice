def get_indices_of_item_wights(arr, limit):
    # 'remember' where all elems located: elem --> [indices]
    elem_indices = dict()
    for index, num in enumerate(arr):
        if num in elem_indices:
            elem_indices[num].append(index)
        else:
            elem_indices[num] = [index]
    # sorting the array
    arr.sort()
    # binary search for the sum of two sum
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        # check the current sum
        lo_elem, hi_elem = arr[lo], arr[hi]
        possible_answer = lo_elem + hi_elem
        # if it matches
        if possible_answer == limit:
            if lo_elem != hi_elem:
                answer = [
                    elem_indices[hi_elem][-1],
                    elem_indices[lo_elem][-1]
                ]
            else:
                # get the indices of both nums
                answer = [
                    elem_indices[lo_elem][-1],
                    elem_indices[lo_elem][-2]
                ]
            return sorted(answer, reverse=True)
        # else, move the indices
        elif possible_answer < limit:
            lo += 1
        else:  # possible_ans > limit
            hi -= 1
    return []
   
  
"""
arr = [4, 6, 10, 15,15, 16],  lim = 21
          ^       ^
          [3, 1]

elem_indices = {
  4: [0],
  6: [1],
  10: [2],
  15: [3,4],
  16: [4]
}

lo = 0
hi = 4

Time - linearithmic (sorting)
space - linear
"""

"""
arr = [4, 6, 6, 15, 16] limit= 12

output = [3, 2] [i, j] i > j

positive ints
indices desc 

Idea #1 - brute 
trying out all the pairs
quadratic

Idea #2

- find the numbers that make up the sum

  # 'remember' where all elems located: elem --> [indices]
  
  {
  4: [0],
  6: [,
  
  }
  # sorting the array
  # binary search for the sum of two sum
  [4, 6, 6, 15, 16]
      ^      ^
  
  - or find it's impossible
    - return []
- find the indices
  # use the indices from the elems in the hash map



"""