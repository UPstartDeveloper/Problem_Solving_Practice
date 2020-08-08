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
    target_cities = [city for city in destinations if city not in origins]  # c^2 iterations
    # we assume there is only one city in the list
    return target_cities[0]


if __name__ == '__main__':
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
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
    