# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
# """

from collections import deque


class PeekingIterator:
    def __init__(self, iterator):
        """
        LeetCode: https://leetcode.com/problems/peeking-iterator/
        
        Initialize your data structure here.
        :type iterator: Iterator
        
        ASSUME: 
            iterator not empty 
            all calls to next() and hasNext() are valid
            
        EC:
            1) multiple calls to peek() in a row?
        
        Solution --> O(1) time and space, amortized
        """
        self.iter = iterator
        self.cache = deque()  # could also just be a list
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if len(self.cache) == 0:
            current_elem = self.iter.next()
            self.cache.append(current_elem) # this len() always <= 1
        return self.cache[0]

    def next(self):
        """
        :rtype: int
        """
        if len(self.cache) > 0:
            return self.cache.popleft()
        return self.iter.next()
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.cache) > 0 or self.iter.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
