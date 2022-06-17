from collections import deque


class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = (
            val, left, right
        )


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def binary_tree_(self, root: BinaryTreeNode) -> int:
        """
        LeetCode: https://leetcode.com/problems/binary-tree-cameras/

        You are given the root of a binary tree. 
        We install cameras on the tree nodes where each camera at a node:
            can monitor its parent, 
                            itself, 
                    and its immediate children.

        Return the minimum number of cameras needed to monitor all nodes of the tree.

        Input: 
            non-null binary tree (any structure)

        Output:
            int - min(num_cameras)

        Intuition:
            maximize(cam) - no leaves, not at root

        Ec:
            root only ==> 1
            null root ==> 0, N/A
            TODO - 

        Approach:
            Idea 1: "alternate"
                every other node in root-leaf path - give it a camera

                Stepping Stone:
                    1: traverse each root to leaf path
                        use a hashset to check for duplicate node visits 

                    2: for each path:
                        num_cameras += 1 for every other node
                    
                    3: num_cameras

        """
        ### HELPERS
        """
            0      
     n   C1      C2
    0    0

        ap 
        []

        cp
        [root, C1,]
        """
        def _traverse_all_r2l_paths(node, current_path, all_paths=[]):
            current_path.append(node)
            # base case
            if not node.left and not node.right:
                all_paths.append(current_path[:])
            # recursive
            else:
                for child in [node.left, node.right]:
                    if child:
                        _traverse_all_r2l_paths(child, current_path, all_paths)
                        current_path.pop()

            return all_paths

        def _place_cameras(all_paths):
            visited = set()
            num_cameras = nc = 0

            for path in all_paths:
                use_camera = 0  # bool flag, false b/c it's root
                for node in path:
                    if use_camera == 1 and node not in visited:
                        nc += 1
                    visited.add(node)
                    use_camera = use_camera ^ 1

            return num_cameras

        def _bfs_solution(root):
            """iterative BFS that counts every other level towards nc"""
            num_cameras = nc = 0
            queue = q = deque([root])

            use_cameras = False

            while queue:
                level_length = len(q)

                if use_cameras:
                    nc += level_length

                for _ in range((level_length)):
                    node = q.popleft()

                    for child in [node.left, node.right]:
                        if child:
                            q.append(child)
                
                use_cameras = True if use_cameras is False else False

            return num_cameras

        def _dfs_solution(node, visited=set(), use_camera=False):
            """recursive pre-order traversal to find camera positions"""
            if node:
                # visit
                if use_camera and node not in visited:
                    self.nc += 1
                visited.add(node)
                # recurse
                next_use_camera = False if use_camera is True else True
                _dfs_solution(node.left, visited, next_use_camera)
                _dfs_solution(node.right, visited, next_use_camera)

        ### GUARD clauses
        if root is None:
            return 0
        elif not root.left and not root.right:
            return 1
        
        ### DRIVER
        # 1: [backtrack]
        self.num_cameras = self.nc = 0

        # 2: "place cameras"
        _dfs_solution(root)

        # 3: all done
        return self.nc
