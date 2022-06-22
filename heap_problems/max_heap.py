class BinaryMaxHeap:
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
                self.items[right], self.items[node_index] = (current, right_elem)
                node_index = right
            # compare parent with left
            elif current < left_elem:
                self.items[left], self.items[node_index] = (current, left_elem)
                node_index = left
            # keep going if needed
            if node_index < len(self.items):
                left, right = self._child_indices(node_index)
                left_elem = self.items[left]
                right_elem = (
                    self.items[right] if right < len(self.items) else float("-inf")
                )
                if self.items[node_index] < max(left_elem, right_elem):
                    self._bubble_down(node_index)

    def _parent_index(self, node_index):
        return (node_index - 1) >> 2

    def _child_indices(self, node_index):
        return [node_index << 1 + 1, node_index << 1 + 2]


if __name__ == "__main__":
    array = [9, 4, 5, 3, 7, 8]
    heap = BinaryMaxHeap(array)
    print(heap.items)
    print(heap.get_max())  # 9
    print(heap.delete_max())  # 9
    print(heap.get_max())  # 8
    heap.insert(4)
    print(heap.get_max())  # 8
    heap.insert(13)
    print(heap.delete_max())  # 13
    print(heap.get_max())  # 8
