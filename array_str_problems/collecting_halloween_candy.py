from collections import deque
from typing import List


class Solution:
    """
    Let's assume it's Halloween, and you're looking to go door to door to collect some candy. 
    You've scoped out the area from prior years, and compiled a list of specific houses that you want to collect candy from.

    You don't want to have to visit every house by yourself,
    - each house only needs to be visited once, so you decide to delegate the work amongst a group. 
    
    
    For your Halloween empire, you've set up the following recursive algorithm to delegate the work:
        - Appoint a candy collector, and give all the work to them
        - Assign titles and responsibilities based on the number of houses they are responsible for 

    Generic: Collector
        Manager   
            If the candy collector is responsible for > 1 house, 
            then they are a manager and can then appoint 
            two candy collectors under them to divide the work 

        Worker
            If the candy collector is responsible for 1 house, 
            then they are a worker and will collect the candy 
            from the houses assigned to them

    Example

        [7, 4, 5, 34] = sum()

    Output --> tree of collectors

    Intuition:
        - divide and conquer
        - recursion --> complete/perfect inary tree

    ASSUME: 
        - subordinate nodes don't need to know their manager

    EC: 
        1) odd number of houses

    Approach:
        1) assign aLL house indices ---> root
        2) recursively:
            - generate the appropite worker node to handle tat subarray of houses
        3) return collectorTree at the end

        Time: O(n)
        Space: O(log n)
    """

    def collect_candy(self, house: List[int]) -> "CollectorTree":
        ### MAIN
        tree = CollectorTree(house)  # init root of tree
        tree.assign_workers()
        return tree


class CollectorNode:
    def __init__(self, parent=None):
        self.parent = parent


class ManagerNode(CollectorNode):
    def __init__(self, house_indices, parent=None):
        self.left, self.right = None, None
        self.hi = house_indices
        super().__init__(parent)


class Worker(CollectorNode):
    def __init__(self, house_index, parent=None):
        self.house_index = house_index
        super().__init__(parent)


class CollectorTree:
    def __init__(self, houses):
        if len(houses) > 1:
            self.root = ManagerNode(range(len(houses)))
        else:
            self.root = Worker(houses)

    def assign_workers(self, boss=None):
        # init case
        if boss is None:
            return self.assign_workers(boss=self.root)
        # recursive: assign more managers
        if isinstance(boss, ManagerNode):
            # divide their work - assume they'll be a manager
            mid_ndx = len(boss.hi) // 2
            boss.left, boss.right = (
                ManagerNode(boss.hi[:mid_ndx], boss),
                ManagerNode(boss.hi[mid_ndx:], boss),
            )
            # conquer: check for more recursion
            for index, node in enumerate([boss.left, boss.right]):
                if len(node.hi) > 1:  # they need to delegate more
                    self.assign_workers(boss=node)
                elif len(node.hi) == 1:  # turns out they're just a worker
                    node = Worker(node.hi[0], boss)
                    # re-establish parent-child relationship
                    if index == 0:
                        boss.left = node
                    else:  # index == 1
                        boss.right = node

    def print_indices(self):
        """Print all the house addresses being collected."""
        # iterative BFS
        visited, q = list(), deque([self.root])
        while q:
            node = q.popleft()
            if isinstance(node, ManagerNode):
                for child in [node.left, node.right]:
                    q.append(child)
            else:  # worker
                visited.append(node.house_index)
        return visited


if __name__ == "__main__":
    houses = [0, 1, 2, 3]
    exp_out = list(range(len(houses)))
    solver = Solution()
    tree = solver.collect_candy(houses)
    assert (
        tree.print_indices() == exp_out
    ), f"Expected: {exp_out}, Actual: {tree.print_indices()}"
