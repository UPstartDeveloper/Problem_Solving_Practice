from collections import deque


def shortest_cell_path(grid, sr, sc, tr, tc):
    # define the 4 directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # UP  # DOWN  # LEFT  # RIGHT
    # starting location, and starting distance
    start = (sr, sc, 0)
    # the dictionary of locations, and distances to the destination
    locations_travelled = set()
    distances_dest = list()
    # init a queue - deque
    next_locations = deque()
    # enqueue the first location, and distance
    next_locations.append(start)
    # as long as the Q's not empty
    while next_locations:
        # dequeue from the queue - # store the location and distance
        next_loc_and_dist = next_locations.popleft()  # (0,0,0)
        next_location_row, next_location_col, dist_so_far = next_loc_and_dist
        # mark the next location as travelled
        locations_travelled.add((next_location_row, next_location_col))
        # check if it's the destination
        if (tr, tc) == (next_location_row, next_location_col):
            # store the distance
            if dist_so_far not in distances_dest:
                distances_dest.append(dist_so_far)
        # iterate over the neighbors, find out where to go next
        for direction in directions:
            delta_x, delta_y = direction
            new_row, new_col = (
                next_location_row + delta_x,
                next_location_col + delta_y,
            )
            # see if we should enqueue the neighboring cell
            neighboring_location = (new_row, new_col, dist_so_far + 1)
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if (
                    grid[new_row][new_col] == 1
                    and (new_row, new_col) not in locations_travelled
                ):
                    # enqueue the neibhor, and location + 1
                    next_locations.append(neighboring_location)
                    print(f"Added {neighboring_location} to the queue")
                    print(distances_dest)
                    print(f"Whole queue: {neighboring_location}")
    # return the min of the destination distances
    min_dist = -1
    if len(distances_dest) > 0:
        min_dist = min(distances_dest)
    return min_dist


grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]

print(shortest_cell_path(grid, 0, 0, 2, 0))


"""

	@param grid: int[][]
	@param sr: int
	@param sc: int
	@param tr: int
	@param tc: int
	@return: int

  BFS - 
  
  find all the 1 paths (u, d, l, r)
  store all the distances
    
  return the min
  
  r = rows
  c= cols
  Time (r * c)
  Space ()
  
  DFS
  
  
  1111
  1001
  1111
  
  {
  
  (0,0): [0], 
  
  
  # Lin Algebra
  (2, 0): [2, 8]
  
  }
  
sr = 0 ----> tr = 2
sc = 0 ----> tc = 0

           0123
      0    1111
      1    0001
      2    1111


s = (0, 0, 0)

locations_travelled = [
  (0,0,0),
]

dd = []

nl = [
  (0, 0, 0),
]

nlr = 0 
nlc = 0
dsf = 0

"""
