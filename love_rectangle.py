"""
Solving the following problem from Interview Cake:
https://www.interviewcake.com/question/python/rectangular-love
"""

"""
1. Restate the problem:
Ok, so you want me to find the overlap between these two rectangles, correct?

2. Clarifying Questions:
Alright, so I see in the example given that the rectangles are in the upper
    right corner of the Cartesian plane. Will the values for the 'left_x' and
    'bottom_y' keys always be positive? Or can these rectangles sometimes go
    into the other corners of the Cartesian plane?

What shall be returned if there is no intersection between the two rectangles?
    Would just an empty dict() object (e.g. {}) suffice?

3. Assumptions:
    For right now, I'll pretend that both of the rectangles always have
    positive integers, as the coordinate values at their vertices.

"""


def make_set(start_coordinate, length):
    '''Compute the set the coordinate values a rectangles takes on an axis.'''
    end_coordinate = start_coordinate + length
    return set(range(start_coordinate, end_coordinate + 1))


def rectangle_love(rect1, rect2):
    '''Computes the overlap between two rectangles in the Cartesian plane.'''
    # Find the intersection of both rectangles on the X-axis, if any
    rect1_x = make_set(rect1['left_x'], rect1['width'])
    rect2_x = make_set(rect2['left_x'], rect2['width'])
    x_intersection = rect1_x.intersection(rect2_x)
    # Do the same for both rectangles in the Y-axis
    rect1_y = make_set(rect1['left_x'], rect1['height'])
    rect2_y = make_set(rect2['left_x'], rect2['height'])
    y_intersection = rect1_y.intersection(rect2_y)
    # construct a new rectanngle dict
    intersected = {}
    return interested
