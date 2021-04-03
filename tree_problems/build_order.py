"""
Build Order: 
You are given a list of projects and a list of dependencies
(which is a list of pairs of projects,
 where the second project is dependent on the first project). 
 
All of a project'sdependencies must be built before the project is. 
Find a build order that will allow the projects to be built. 

If there is no valid build order, return an error.

EXAMPLE 

Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) 

Output: f, e, a, b, d, c

1. multiple answers? yes
    - does the stdout have to be on one line?
2. what kind of error? ValueError
3. assume each project - 1 dep? yes
4. assume every project can have <= 1 dep
5. and +1 project can have the same dep? yes
6. not a binary tree? yes
7. can a project also be a dep? yes
8. so isolated nodes can be anywhere?
9. return value? none
10. does every package have a unique name? yes
11. can branches intersect? yes

Intuition: guessing
- valid build orders are DAG (tree)
- invalid build orders contain cycles

parent - dep
child - project

each package is it's own node

   f
/     \  
a      b   
\    /
  d
   \
     c

Approach:
# - build an Mway tree of the projects and their dependencies
    # adjacency list - each node could have a dict or a list of its children
    # 
# - then print the tree in BFS order

# - then print any remaining nodes

class BuildTree
    - root 
    - dict of nodes (or island packages)

class PackageNode:
    - name
    - array of children
    - set
        - ops I care about
            - need to be able to traverse the set fast
            - add to the children 
            - go w/ array for debugging purposes (slightly slower on small datasets)
"""
from collections import deque
from typing import List, Tuple


class PackageNode:
    def __init__(self, key: str):
        self.key = key
        self.users = list()  # List[PackageNode]
        self.dependencies = list()


class BuildTree:
    def __init__(self, projects, dependencies):
        # self.root = None
        self.packages = dict(
            zip(
                projects,
                [PackageNode(p) for p in projects] 
            )
        )
        self.add_dependencies(dependencies)

    def add_dependencies(self, dependencies):
        # iterate over the dependencies
        for dependency_str, project_str in dependencies:
            # get the project and dependency
            project, dependency = (
                self.packages[project_str],
                self.packages[dependency_str]
            )
            # add project as child of dependency
            dependency.users.append(project)
            # record the dependency of the project
            project.dependencies.append(dependency)

    def _find_root(self, visited: set):
        for package in self.packages.values():
            if len(package.dependencies) == 0 and package not in visited:
                return package
        else:
            raise ValueError("Couldn't resolve build order, \
                            most likely due to a cyclical dependency.")

    def _bfs_connected_components(self, visited, output, q, root) -> None:
        # enqueue the first node
        q.append(root)
        # traverse
        while q:
            # dequeue a node
            node = q.popleft()
            # visit it
            output.append(node)
            visited.add(node)
            # enqueue the unvisited neighbors
            for user in node.users:
                if user not in visited:
                    q.append(user)

    def show_build(self) -> str:
        # init collections - queue and set, and array for the output
        output = list()
        q = deque()
        visited = set()
        # traverse - until all the nodes are visited
        while len(visited) < len(self.packages):
            # choose a node - check if it's a root (in-degree of zero?)
            root = self._find_root(visited)
            # BFS the set of connected components
            self._bfs_connected_components(visited, output, q, root)
        return output


class Solution:
    def build_order(projects: List[str], dependencies: List[Tuple[str]]) -> None:
        # A: TODO: build the tree of the tree order
        build_order = BuildTree(projects, dependencies)
        # B: print out the nodes via BFS, and the remaining ones
        print(build_order.show_build())
        return


"""
projects: a, b, c, d, e, f
dependencies: 
     d  p
    (a, d), <
    (f, b), <
    (b, d), <
    (f, a), <
    (d, c) 

bo
packages = {
    "a": {
        users: [d, ],
        d: [f, ]
    }
    "b": {
        users: [d ],
        d: [f]
    }
    "c": {
        users: [],
        d: [d, ]
    }
    "d": {
        users: [c],
        d: [a, b]
    }
    "e": {
        users: [],
        d: []
    }
    "f": {
        users: [a, b],
        d: [, ]
    }
}

"""
