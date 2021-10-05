#!/usr/bin/env python3

# the above line is a shebang, and an optional comment placed at the top of a Python
# script. This particular shebang is for Python 3. It enables this script to be
# executed without needing to type `python` first in the command line (or when clicking)
# on it on a file manager

# Source for above information: https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

"""
Problem: 
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

input:
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

output:
"Sao Paulo"

"""
from typing import List


# Idea #1: using Lists
# Time is Quadratic
# Memory is O(n) - linear
def get_destination_city(paths):
    # create two lists, one for origin cities and the destination cities
    origins, destinations = list(), list()  # O(1)
    for path in paths:  # p iterations, where p = # of paths
        origin, destination = path  # O(1)
        # add the cities to the appropiate list, if they are unique
        if origin not in origins:  # c/2 = 2p/2 = p iterations
            origins.append(origin)
        if destination not in destinations:  # p iterations
            destinations.append(destination)
    # find the city which is a destination of a path, but the origin of one
    target_cities = [
        city for city in destinations if city not in origins
    ]  # c^2 iterations
    # we assume there is only one city in the list
    return target_cities[0]


# Idea 2: using a dict
# Time is still quadratic
# memory is still linear

# paths = [   [outlink, inlink]    ] -> city with no outlink
def get_destination_city(paths):
    city_outlinks = dict()
    # iterate over the paths, add the cities and number of outlinks
    for path in paths:  # p iterations
        # unpack the path into the origin and destination city
        origin, destination = path
        # add origin to the dictionary
        if origin in city_outlinks:  # c iterations = 2p
            city_outlinks[origin] += 1
        else:  # origin city is not yet in city_outlinks
            city_outlinks[origin] = 1
        # add destination to the dictionary
        if destination not in city_outlinks:  # c iteration = 2p
            city_outlinks[destination] = 0
    # find the city with no outlinks
    for city in city_outlinks:
        if city_outlinks[city] == 0:
            return city


# Idea 3: Using OOP:
"""
Complexity Analysis:

Time: linear 
The runtime of this function scales linearly as the number of paths, p, 
which the airline company serves asymptotically increases. Therefore the
runtime can be expressed as O(3p), which simplifies to O(p).

Space: linear
The additional memory used by this solution rises in linear proportion to 
number of cities, or c (which equals 2p), which the computer needs to allocate
memory for during execution. Therefore the space complexity can be expressed as 
O(p), because the memory will grow linearly the size of the input asymptotically
grows. Unfortunately this linear space complexity is also more expensive than
the linear space complexities of the previous two solutions, because it uses 
custom Python classes rather than just the built-in data types. It is still in
the same complexity class, but regardless in production environments it will
be more expensive by a certain coefficient (which can be determined by
benchmarking). 

"""


class City:
    """
    For now, all this class will do is
    store the numbers of inlinks/outlinks that
    a city has, not the cities those links
    come from/go to.
    """

    def __init__(self, city_name):
        self.city_name = city_name
        self.inlinks = self.outlinks = 0


class Airline:
    def __init__(self):
        self.cities = dict()  # str -> City obj

    def set_paths(self, path):
        # iterate over the path
        for path in paths:  # p iterations
            # make city objects
            origin, destination = path
            origin_city, destination_city = (City(origin), City(destination))
            # increment the inlink/outlink properties
            origin_city.outlinks += 1
            destination_city.inlinks += 1
            # add to the overall object dictionary
            self.cities[origin] = origin_city
            self.cities[destination] = destination_city
        # return the city with no outlinks
        for city in self.cities:  # c iterations = 2p iterations
            city_outlinks = self.cities[city].outlinks
            if city_outlinks == 0:
                return city


if __name__ == "__main__":
    paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    print(get_destination_city(paths))

"""
Variable Value Trace:

paths = [
    ["London","New York"],
    ["New York","Lima"],
    ["Lima","Sao Paulo"]
]

origins = ["London", "New York", "Lima"]

destinations = ["New York", "Lima", "Sao Paulo"]

Complexity Analysis:

p  = # paths
c = # of cities = 2p
Time:
    The runtime of this function rises linearly in propo
"""
