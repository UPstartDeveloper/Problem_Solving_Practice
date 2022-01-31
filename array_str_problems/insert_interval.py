class Solution:
    """
    Given a sorted set of intervals 
        (sorted based on the 1st value of a given range) 
        that do not overlap, 
        
    Write a function to insert a new interval into the set of intervals. 
    You can merge values in the sorted set to accommodate the new interval. 
    
    Below are a few examples:
    
    Example 1:
        Set of intervals: [1, 2], [7, 10]
        Insert: [2, 5]
        New set of intervals: [1, 5], [7, 10]
  
    Example 2:
        Set of intervals: [1, 2], [4, 7], [8, 10], [12, 16]
        Insert: [4, 9]
        New set of intervals: [1, 2], [4, 10], [12, 16]
   
    Example 3:
        Set of intervals: [1, 2], [2,3] [3, 7]
        Insert: [4, 9]
        New set of intervals: [1, 2], [4, 9]
                                I------I
                        X-------X               X------------X
    <------------------------------------------------->
                0       1       2      5        7           10


    Input: 2D int[arr, unique, immutable]
    Output:
        - same no. of rows (or less)
        - merging 

    Intuition:
        insert - overlap w/ 1+ of input

    Stepping Stone:

        1) given a set of interval --> any kind of algo
            1) insert: [>=the end of one interval, less<= start of next interval]
            2) merge intervals algo
        2) 

    EC:
        ASSUME: can add intervals where start == end
    """
    pass