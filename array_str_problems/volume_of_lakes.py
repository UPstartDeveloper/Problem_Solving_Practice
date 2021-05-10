"""
Imagine an island that is in the shape of a bar graph. 

When it rains, certain areas of the island fill up with rainwater to form lakes. 
Any excess rainwater the island cannot hold in lakes will run off the island 
to the west or east and drain into the ocean.

Given an array of positive integers representing 2-D bar heights, 
design an algorithm (or write a function) 
that can compute the total volume (capacity) of
water that could be held in all lakes on such an island given an array of the heights of the bars. 

Assume an elevation map where the width of each bar is 1.
                0  1  2  3  4  5  6  7  8  9  0  1  2  3  4
Example: Given [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2], 
               [W, L, W, L, W, W, W, L, L, W, W, W, L, W, W]
return 15 (3 bodies of water with volumes of 1,7,7 yields total volume of 15)


Clarifying questions
1. Elevation map? ==> no worries, use len(input) as x-axis and array values for y-axis

Intuition:
optimization problem

Lakes have following properties
- form over indices whose elements are less than both their neighbors by >= 1
- max water level (before run-off) of a lake is min(left, right) for the land elements 
    enclosing the lake

Approach:

A: find each lake
    1. label indices as (land == 1) or (water == 0)
        a. approach: start off at first index where land > first index
                     end at the last index where land > last index
                     label the start as land --> find next index where height >= start_height
                        - everything in between is water
                        - repeat until you reach end land
                     # convert list of labels --> list of enclosing indicies
                    # approach for this!
                        # A: go from first L to last L in the list
                        # B: if L before W, that's a starting index (the former)
                        # C: if W before L, that's an ending index (the latter)
                        # D: append the (start, end) to a list
B: compute the max vol. of each lake
    input - indices of the land enclosing left and right sides of the lake
    approach - compute water_height; culm. sum of (water_height - each water index)
C: compute and return total vol of whole island
    1. approach:
        # init total
        # pass the indices to (B), add to the total
        # return the total

Edge Cases:
- empty array? --> return 0
- zero or negative values? --> ValueError
- all duplicates? --> return 0
- sorted order --> return 0
- single peak (e.g [1,1,1,1,5,1,1,1]) --> return 0
"""
from typing import List


def volume_of_lakes(island: List[int]):
    '''Linear time and space solution'''

    def find_lake_locations(labels, land_start_index, end_land_index):
        """TODO: add docstring
        """
        lake_locations = list()
        if land_start_index < end_land_index:
            # A: go from first L to last L in the list
            index = land_start_index
            location = []
            while index < end_land_index:
                if index < len(labels) - 1:
                    label, next_label = labels[index], labels[index + 1]
                    # B: if L before W, that's a starting index (the former)
                    if label == 1 and next_label == 0:
                        location.append(index)
                    # C: if W before L, that's an ending index (the latter)
                    elif label == 0 and next_label == 1:
                        location.append(index + 1)
                    # D: append the (start, end) to a list
                    if len(location) == 2:
                        lake_locations.append([i for i in location])
                        location = []
                index += 1
        return lake_locations

    def find_lakes():
        """water == 0; land == 1"""
        labels = [0 for _ in range(len(island))]
        # start off at first index where land > first index
        land_start_index = 0
        init_height = island[0]
        while land_start_index < len(island):
            if island[land_start_index] <= init_height:
                land_start_index += 1
        # end at the last index where land > last index
        end_land_index = -1
        if land_start_index < len(island):
            final_height = island[-1]
            end_land_index = len(island) - 1  # TODO: rename var to be consistent
            while end_land_index > land_start_index:
                if island[end_land_index] <= final_height:
                    end_land_index -= 1
            # in case the heights are same, then the last index really is the end
            if island[end_land_index] == island[-1]:
                end_land_index = len(island) - 1
        # label the island as land or water
        if end_land_index > land_start_index:
            # label the start and end as land --> 
            labels[land_start_index] = labels[end_land_index] = 1
            land_height = island[land_start_index]
            index = land_start_index + 1
            # find next index where height >= start_height
            while index < end_land_index:
                height = island[index]
                # land found
                if height >= land_height:
                    labels[index] = 1
                    land_height = height
                # move to next index
                index += 1
        # convert list of labels --> list of enclosing indicies
        return labels, land_start_index, end_land_index

    def compute_volume(start, end):
        volume = 0
        if start < end:
            # compute lake height
            lake_height = min(island[start], island[end])
            # compute lake volume
            for index in range(start + 1, end):
                volume += lake_height - island[index]
        return volume

    # A: guard clauses to validate input
    if len(island) == 0:
        return 0
    # B: find each lake
    labels, land_start_index, end_land_index = find_lakes()
    lake_locations = find_lake_locations(labels, land_start_index, end_land_index)
    # C: compute and return total vol of whole island
    total = 0
    for start, end in lake_locations:
        total += compute_volume(start, end)
    return total


"""
Variable Heap: 

island = 
 0  1  2  3  4  5  6  7  8  9  0  1  2  3  4
                                     v
[1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]
                         ^           ^      
v = 0, 1
    0, 3, 4, 7
    0, 2, 4, 7

ll = [
    [1, 3],   <
    [3, 7],   <
    [8, 12]   <
]

t = 0, 1, 8, 15


labels =
 0  1  2  3  4  5  6  7  8  9  0  1  2  3  4
    v                                v
[0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0]
                                     ^  ^
[W, L, W, L, W, W, W, L, L, W, W, W, L, W, W]

lsi = 0,      1
eli = -1, 14, 12
i = 1

l = [1, 3], [3, 7], [8, 12]

ih = 1

fh = 2

i = 2
lh = 5



"""
