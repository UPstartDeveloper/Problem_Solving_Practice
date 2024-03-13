# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# link to full Leetcode page: https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/	
class Solution:
   def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
       """
       Intuition: binary search


       Assumptions
           - can't assume the query in tree
           - if query in tree ---> give same for min/max
          
       Approach:


       1) 2 BS's for each query


           - 1st attempt lookup
               if found val --> return the tree node
               if not val ---> [visited nodes]
                       16 ---> [6, 13,   15] -1
                                        min
                                              max
       Pseudocode:
       visited = [6, 13, 15]
           helper - recursive BS


               input: current node = root, target


               body:
               if current:
                   visited.append(root.val)
               else:
                   return visited
               if current and current.val == target
                   return visited
               if current and current.val > target:
                   recurse(current.left)
               if current and current.val < target:
                   recurse(current.right)           
       """
       ### HELPER(S)
       def _search(
           current: "TreeNode",
           minimum: int,
           maximum: int,
           target: int
       ):
           if current:
               if current.val <= target:
                   minimum = max(minimum, current.val)
               if current.val >= target:
                   maximum = min(maximum, current.val)
           else:
               return minimum, maximum
           if current and current.val == target:
               return target, target
           if current and current.val > target:
               return _search(current.left, minimum, maximum, target)
           if current and current.val < target:
               return _search(current.right, minimum, maximum, target)  


       def _traverse(visited: list, query: int):
           """
           visited = [6, 13, 15]
                                ^
           q = 16


           mini = 15
           maximum = -1


           min_index = 2
           max_index = 3
           """
           # 2x linear search
           mini, maximum = -1, -1
           if len(visited) > 0:
               visited.sort()
               min_index = len(visited) - 1
               while min_index > -1:
                   if visited[min_index] <= query:
                       break
                   else:
                       min_index -= 1
               if min_index != -1:
                   mini = visited[min_index]
              
               #
               max_index = 0
               while max_index < len(visited):
                   if visited[max_index] >= query:
                       break
                   else:
                       max_index += 1
               if max_index == len(visited):
                   maximum = visited[max_index]
           return mini, maximum   # 15, -1


       ### DRIVER
       output = [[-1, -1] for _ in queries]


       if root:
           # populate each row of output
           for index, query in enumerate(queries):
               minimum, maximum = _search(
                   root, float("-inf"), float("inf"), query
               )
               if minimum != float("-inf"):
                   output[index][0] = minimum
               if maximum != float("inf"):
                   output[index][1] = maximum


       # done
       return output
