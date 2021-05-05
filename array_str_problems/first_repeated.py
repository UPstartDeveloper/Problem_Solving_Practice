"""
Suppose you're given an array of integers. 
Write code to find the first repeating element in the array.

For example:
 
Input: array = [10, 2, -2, -20, 10]  
Output: 10
      
Input: array = [9, 4, 20, 20, 10, 5]   
Output: 20
       
If there are no duplicates, you can return -1.


-------
ASSUME the input is mutable

Intuition - search problem

Approach:

1) Brute Force - nested for loops
2) HashSet - if item already in set, return it
3) Sorting - better time than 1) (not 2), better memory than 2

Edge Cases:
1) pos/neg - normal
2) dupes - normal
3) []? --> return -1
4) not int --> ValueError
"""
