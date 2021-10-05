"""
Problem:

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

"""

# def isBadVersion(version):
#   return version > 7
# when you run your tests, comment this function out.

"""
last_version = 5 -> means n = 5
our list of versions could look like

 0  1  2  3  4 
[1, 2, 3, 4, 8]

- We're returning the index?

 0  1  2  3  4 
[1, 2, 3, 4, 8]

LESSONS LEARNED
 - read the question! make sure you understand what you're being asked
     - read the example, if it's given - it's ok if at the beginning you only understand at a high level
 - trace your code! 
 
Rules about the problem
  - version counting starts at version no. 1
  - we want to find the lowest version no. that returns True
  
  
Idea #1

n = last_version
- create a list of range(1, n + 1) to represent the versions -> [1, 2, 3, 4, 5]
- iterate from the back
  - store variable for the index of versions that return True
    - update it as you go through the list in reverse
- return index + 1, or versions[index]

Time: O(n) (n API calls)
Space: O(n)

Idea #2 - use example algorithm

anytime the API returns False, move further in the version line (all previous are true)
anytime the API return True, move backward, until you reach just 1 past the last True 

- make the range
- start iterating from the middle
  - go till the end/front, iterate over that range
  
Idea #3 - modified binary search
 0  1  2  3  4
[1, 2, 3, 4, 5]
 F  F  F  F | T

keys:
- there's a specific boundary where the firstBadVersion occurs
  - it's after every False
  - before every True

A: make the versions array
B: start at the middle index
  - if False, move the range to everything to the right of the index
      - store lowest false index in a dict: {lowest_false: index}
      - update as needed
    - start iterating that range in reverse
      - if you hit the index just after the lowest false, then return the index
  - if True - move back
  
Idea #4 - simplified idea #3
A: make the versions array
B: start at the middle index
  - if False, right until you hit True
    - update the variable storing highest False index
      - if you hit the index just after the highest false, then return the index
  - if True - move back until you hit a False 
  
in another way:

if False:
  # iterate backwards over the range(index_lowest_false, index_highest_true)
      - go until you revisit that False, or one that's after it
      - as you go, update the index of the lowest True

"""
import math


def firstBadVersion(last_version, isBadVersion):
    # assume the last_version is bad
    lowest_true = last_version
    # find the middle to start iterating from (middle between 1, and last_version)
    highest_false = math.ceil(last_version / 2)
    # find the last working version
    while isBadVersion(highest_false) is True:
        # iterate forwards
        highest_false -= 1
        # find the last bad version
    while lowest_true > highest_false:
        if isBadVersion(lowest_true) is True:
            # update the lowest_true, and iterate again
            lowest_true -= 1
    # we found it!
    return lowest_true + 1


"""
last_version = 5

[F, F, F, F, T]

lowest_true  |  highest_false   |
    5                 3
                      4
    
"""
