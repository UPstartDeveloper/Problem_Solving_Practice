from collections import deque
import math


class BinaryHeap:
    def __init__(self, items=None):
        self.items = list()
        if isinstance(items, list) and len(items) > 0:
            for item in items:
                self.insert(item)

    def get_max(self) -> int:
        if self.size() > 0:
            return self.items[0]

    def delete_max(self) -> int:
        if self.size() > 0:
            # copy the max,
            last_index = len(self.items) - 1
            # switch it with a leaf.
            highest, leaf = self.get_max(), self.items[last_index]
            self.items[0], self.items[last_index] = leaf, highest
            # Then, delete it.
            self.items.pop()
            # reorder the tree
            if self.size() > 1:
                self._bubble_down(0)

            return highest

    def insert(self, new: int) -> None:
        self.items.append(new)
        if self.size() > 1:
            self._bubble_up(self.size() - 1)

    def size(self):
        return len(self.items)

    def _bubble_up(self, node_index):
        # grab the item at the current index
        current = self.items[node_index]
        # grab its parent element
        if node_index > 0:
            parent_index = self._parent_index(node_index)
            parent = self.items[parent_index]
            # swap if needed
            if current > parent:
                self.items[parent_index] = current
                self.items[node_index] = parent
                # recurse if needed
                if parent_index > 0:
                    self._bubble_up(parent_index)

    def _bubble_down(self, node_index):
        current = self.items[node_index]
        if node_index < len(self.items):
            left, right = self._child_indices(node_index)
            left_elem = self.items[left]
            if right < len(self.items):
                # compare parent with right
                right_elem = self.items[right]
            if right_elem > current and right_elem > left_elem:
                self.items[right], self.items[node_index] = current, right_elem
                node_index = right
            # compare parent with left
            elif current < left_elem:
                self.items[left], self.items[node_index] = (current, left_elem)
                node_index = left
            # keep going if needed
            if node_index < len(self.items):
                left, right = self._child_indices(node_index)
                left_elem = self.items[left]
                right_elem = self.items[right]
                if (
                    self.items[node_index] < left_elem
                    or self.items[node_index] < right_elem
                ):
                    self._bubble_down(node_index)

    def _parent_index(self, node_index):
        return (node_index - 1) >> 2

    def _child_indices(self, node_index):
        return [node_index << 1 + 1, node_index << 1 + 2]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """LeetCode: https://leetcode.com/problems/k-closest-points-to-origin"""

        ### HELPERS
        def _get_dist(x, y):
            return (x ** 2) + (y ** 2)

        ### DRIVER

        # Assume that n >= k > 0

        # A: get dists
        point_dist = [_get_dist(x, y) for x, y in points]

        # B: "bucket" distances by dist -> indices of points
        dist_buckets = db = dict()
        for index, dist in enumerate(point_dist):
            if dist not in db:
                db[dist] = deque([index])
            else:
                db[dist].append(index)

        # C: sort the distances using a heap
        heap = h = BinaryHeap(point_dist[:k])  # max heap
        for i in range(k, len(point_dist)):
            dist = point_dist[i]
            if dist < heap.get_max():
                heap.delete_max()  # TODO[debug]
                heap.insert(dist)  # TODO[debug]

        k_lowest_dists = kld = heap.items[:]

        # D: convert the sorted distances back into point objs
        k_lowest_points = klp = list()
        for dist in kld:
            index = db[dist].popleft()
            klp.append(points[index])

        return klp
