from typing import List


class NestedInteger:
    """
    LeetCode: https://leetcode.com/problems/flatten-nested-list-iterator/
    This is the interface that allows for creating nested lists.
    You should not implement it, or speculate about its implementation
    """

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> List["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        # recursive backtracking algo
        self.all_ints = list()
        self._populate(0, nestedList)  # TODO[test]
        self.global_index = 0

    def _populate(self, index, current_list):
        """recursive backtrackig on an m-way"""
        if index < len(current_list):
            element = current_list[index]

            # base case: is an int
            if element.isInteger():
                self.all_ints.append(element.getInteger())
            # recursive case: is a list
            else:
                nested_list = element.getList()
                # for new_index in range(len(nested_list)):
                self._populate(0, nested_list)
            return self._populate(index + 1, current_list)

    def next(self) -> int:
        element = self.all_ints[self.global_index]
        self.global_index += 1
        return element

    def hasNext(self) -> bool:
        return self.global_index < len(self.all_ints)


"""
all_ints = [1, 1, 2, 1, 1]

nestedList = [[1,1],2,[1,1]]
                      ^
nested_list = [1,1]
               
index
1

current_list
[[1,1],2,[1,1]]


"""
