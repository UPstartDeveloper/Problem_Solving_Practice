def calc_drone_min_energy(route):
    """

    e minimum amount of energy req for flight

    energy
    input:  route = [ 
                    x    y   z
                    [0,   2, 10],  0, total = 0
                    [3,   5,  0], +10 energy, total= 10 
                    [9,  20,  6], -6 energy, total = 4
                    [10, 12, 15], -9 energy, total = 
                    [10, 10,  8] ] +7 energy, total = 2
                    
                    2 energy

    output: 5 # less than 5 kWh and the drone would crash before the finish
            # line. More than `5` kWh and it’d end up with excess energy
            
            
    approach:

    - iterate over all the points
    - store the totals in an array
    - find the lowest at the end
    - if min < 0:
        - return min * -1
    if min >= 0:
        - return 0
    """
    # A: iterate over all the points
    total = 0
    current_alt = route[0][2]
    min_total = total
    for index, point in enumerate(route):
        x, y, z = point
        # B: update the minimal energy in the route
        if index > 0:
            new_alt = z
            total = total + (-1 * (new_alt - current_alt))
            current_alt = new_alt
        if total < min_total:
            min_total = total
    # C: find the lowest at the end
    return -1 * min_total
  
"""
route = [ 
   x    y   z
  [0,   2, 10],  0, total = 0
  [3,   5,  0], +10 energy, total= 10 
  [9,  20,  6], -6 energy, total = 4
  [10, 12, 15], -9 energy, total = 
  [10, 10,  8] ] +7 energy, total = 2
  
t = 0, 10, 4, -5, 2
ts = [0, 10, 4, -5, 2]

ca = 10, 0, 6, 15
na = 0, 6, 15, 8
p = [0,   2, 10], 
    [3,   5,  0],
    [9,  20,  6]
    [10, 12, 15]
    [10, 10,  8]

Time: O(n)
Space: O(1)
"""