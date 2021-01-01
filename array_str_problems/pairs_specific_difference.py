def find_pairs_with_given_difference(arr, k):
  intermediate = list()
  # A: use 2 for loops to find those triplet, and put them in a 2D array
  for index, element in enumerate(arr):
    for other_index, other_elem in enumerate(arr):
      if index != other_index:
        if element - other_elem == k:
          triplet = [element, other_elem, other_index]
          intermediate.append(triplet)
  # B: sort the intermediate by the z-axis - nlogn
  intermediate.sort(key=lambda triplet: triplet[2])
  # C: list comp to get the x, y elems - n
  output = [
    [triplet[0], triplet[1]] for triplet in intermediate 
  ]
  return output

def find_pairs_with_given_difference_linear(arr, k):
  elements = set(arr)
  
  output = list()
  # element = x
  # element - k = y
  
  for element in arr:
    if (element - k) in elements:
      output.append([(element - k), element])
      
  return output

"""
O(n)
O(n)

 arr = [0, -1, -2, 2, 1], k = 1
 
 {
  y: x
  0: 0, 
 -1: 1,
 -2: 2, 
  2: 3, 
  1: 4
 }
 
output = [
  # [0, -1], [-1, -2], [2, 1], [1, 0]
  
  [-1, 0], [-2, -1], [1, 2], [0, 1]
]

e = 0, -1, -2, 2
"""


"""

 arr = [0, -1, -2, 2, 1], k = 1
 
 { 
  0, -1, -2, 2, 1
 }
 
 output = [
    [0, -1], 1
 ]
 
 
 
 
 
 
 
 
 
 
 
 inter = [[0, -1, 1], ]

index     e      oi     oe
0         0       0      0
                  1      -1




output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

"""
"""
unsorted
no dupes
arr maybe also empty


main the ordering of the second elements 

       0   1   2  3  4
arr = [0, -1, -2, 2, 1], 
k = 1
     0
[[1, 0], [0, -1], [-1, -2], [2, 1]]

Brainstoriming:

1. Quadratic solution:

Intutition: try every combo of two integers
Approach:
  # A: use 2 for loops to find those triplet, and put them in a 2D array
  # B: sorting the pairs
    # sort the intermediate by the z-axis - nlogn
    # list comp to get the x, y elems - n

intermediate = [
  [0, -1, 1], [1, 0, 0], [-1, -2, 2], [2, 1, 4]
]    

intermediate = [
  [1, 0, 0], [0, -1, 1], , [-1, -2, 2], [2, 1, 4]
]  

output =  [[1, 0], [0, -1], [-1, -2], [2, 1]]


arr = [0, -1, -2, 2, 1], 

i = 1
j = 4
i != j


[0, -1, -2, 2, 1]

[(-2, 2), (-1, 1), (0, 0), (1, 4), (2, 3)]
                     ^       ^
  2 - (-2) = 4
  1 - (-2) = 3
  0 - (-2) = 2
  -1 - (-2) = 1
  

"""