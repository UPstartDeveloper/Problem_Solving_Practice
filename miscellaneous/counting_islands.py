from collections import deque


def get_number_of_islands(binaryMatrix):
    def is_land(current_row, current_col):
        # get the current vertex at this position
        vertex = binaryMatrix[current_row][current_col]
        # if it's zero, return False
        return vertex == 1

    def get_available_neighbors(current_row, current_col):
        # init list of neighbors
        neighbors = list()
        # check each position in the 4 directions
        for direction in directions:
            direction_x, direction_y = direction
            # calculate the indices of the neighbor
            neighbor_row = current_row + direction_x  # 0
            neighbor_col = current_col + direction_y  # 2
            # validate it
            if (
                (neighbor_row, neighbor_col) not in visited
                and 0 <= neighbor_row < NUM_ROWS
                and 0 <= neighbor_col < NUM_COLS
            ):
                neighbors.append((neighbor_row, neighbor_col))
        return neighbors

    """
  - is it always a square matrix? no
  - diagonal connection - does NOT mean that the 1's are part of the same island
  - types: given 2D array, return int
  - input is immutable
  
  - question:
    - whole matrix is kinda like a graph
      - we have data (the 1's specifically) can connect to each other is different ways, and it's not 
        necessarily linear
    - each element is the matrix can be thought of a vertex
    - the edges of each vertex is its neighbor in each of the 4 cardinal directions
    - each island = set of connected components
    - What the questions is really asking us is to find the number of connected components in the graph
    
    - Vertex = element in the matrix, which can access with indices [x][y], where 
                0 < x < num_rows, 0 < y < num_cols
    Idea #1: BFS
    A: getting the data structures
    - init a queue, for the vertices to visit next
    - init a set: visited - to keep track of the vertices we've already seen
    - init a count = 0 - num of components that we have 
    B: traverse the matrix
      - on every element, start by adding its indices to the set of visited
      if it's a zero - move on
      if it's a one:
          - find out which of its neighbors are "available"
            - if we run into IndexErrors, and not in the visited set
          - enqueue those neighbors
          - while the queue is not empty:
            - deque from that queue
              - check if it's zero or 1, do the same for BFS
              
          - increment the number of islands
    
      for 0 -> move
      for 1 ->
        check all the neighbors
     C: return the number of islands
     
     Time Complexity:
     O(V + E) - linear for time
     Space Complexity
     O(V) - visited set
        
     
    
    
    Q =
    
    front [left_neighbor, right_neighbor, down_neighbor] back 
    
    V =
    {(0, 0), (0,1), (1, 1), (0, 2), }
    
    current_island_vertices = 
    
    count = 1
    
    current_row = 0, current_col = 3
    
  
  """  # your code goes here
    # A: getting the data structures
    # init a queue, for the vertices to visit next
    next_vertices = deque()

    # init a set: visited - to keep track of the vertices we've already seen
    visited = set()
    # init a count = 0 - num of components that we have
    islands = 0
    # B: traverse the matrix
    # define directions
    NUM_ROWS = len(binaryMatrix)
    NUM_COLS = 0
    # update number of columns - overcome the assumption of >= 1 rows
    if NUM_ROWS > 0:
        NUM_COLS = len(binaryMatrix[0])
    current_row, current_col = 0, 0
    RIGHT, LEFT, UP, DOWN = ((0, 1), (0, -1), (-1, 0), (1, 0))
    directions = [RIGHT, LEFT, UP, DOWN]
    # - on every element, start by adding its indices to the set of visited
    while current_row < NUM_ROWS:
        while current_col < NUM_COLS:
            # if it's not, just move on
            if (current_row, current_col) not in visited and is_land(
                current_row, current_col
            ) is True:
                # get_available_neighbors
                neighbors = get_available_neighbors(current_row, current_col)
                # enqueue those neighbors
                for neighbor in neighbors:
                    next_vertices.append(neighbor)
                # while the queue's not empty
                while next_vertices:
                    # dequeue the next vertex
                    next_vertex = next_vertices.popleft()
                    next_row, next_col = next_vertex
                    if (next_row, next_col) not in visited and is_land(
                        next_row, next_col
                    ) is True:
                        neighbors = get_available_neighbors(next_row, next_col)
                        # enqueue those neighbors
                        for neighbor in neighbors:
                            next_vertices.append(neighbor)
                    visited.add(next_vertex)
                islands += 1
            # mark the current position as being visited
            visited.add((current_row, current_col))
            # increment the col no matter what
            current_col += 1
        current_col = 0
        current_row += 1
    return islands


"""
current_vertix = binaryMatrix[current_row][current_col]
if it's a zero - move on
if it's a one:
    - find out which of its neighbors are "available"
      - if we run into IndexErrors, and not in the visited set
    - enqueue those neighbors
    - while the queue is not empty:
      - deque from that queue
        - check if it's zero or 1, do the same for BFS

    - increment the number of islands

for 0 -> move
for 1 ->
  check all the neighbors
C: return the number of islands


Variable Value

 NUM_ROWS = 5
 NUM_COLS = 5
   islands   | cr, cc  
    2       |  0, 5  
next_vertices   |   visited  
[, (1, 4)  ]              |      { (0, 0), (0, 1), (0, 2), (1, 1), (0, 3),
                                                 (0, 4), (1, 3), (1, 2), (2, 3), (1, 4), (0, 4)} 

neighbors = [ (0, 2), (1, 1)]



[[1,0,1,0],
 [0,1,1,1],
 [0,0,1,0]]
 
 
 Variable Value
 
 [[1, 0, 1, 0]]
 
 NUM_ROWS = 1
 NUM_COLS = 4
 islands = 2
 cr   cc
 0    0
 
 
next_vertices = [ ]
visited = { (0, 1), (0, 0), (0, 3) }
"""
