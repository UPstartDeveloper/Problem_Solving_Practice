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
    """
    Idea 1: using Sets
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

    oh no! this data structure won't let be able to pull out either the
    the bottm_y or left_x
    """
    """
    Idea 2: using iteration

    1. have some control variable, like continue = True
       a. while continue is True, we iterate over the range of coordinate
          values that each rectangle occupies along that axis
       b. if we see a matching coordinate, then we want to see how wide/high
          it goes. We can then break, and move on to the following steps:
          - compute the final coordinate that each rectangle occupies on
            the axis
          - compare them to see which is smaller
          - calculate the distance from the start of the intersection, to the
            smaller final coordinate
       c. if no match occurs, then return None for that axis

    """
    def access_edge(rect, start, length):
        """Return the starting coordinate value, and length of the rectangle
           occupies on some axis.

        """
        return rect[start], rect[length]

    def find_axis_overlap(axis):
        '''Compute the location of two rectangles' overlap on an axis.'''
        # determine the axis we are traversing
        if axis == 'x':
            start, length = 'left_x', 'width'
        elif axis == 'y':
            start, length = 'bottom_y', 'height'
        # obtain values from each rectangle for this axis
        rect1_start, rect1_length = access_edge(rect1, start, length)
        rect2_start, rect2_length = access_edge(rect2, start, length)
        # calculate the final coordinate values for both rectangles on the axis
        rect1_final, rect2_final = (
            rect1_start + rect1_length + 1
            rect2_start + rect2_length + 1
        )
        # make a range of the second rectangles coordinate values
        rect2_range = range(rect2_start, rect2_final)
        # find if any overlap occurs
        rect1_coordinate, intersected_length = rect1_start, 0
        while rect1_coordinate > rect1_final:
            if rect1_coordinate in rect2_range:
                # determine the length of the overlap
                if rect1_final <= rect2_final:
                    intersected_length = rect1_final - rect1_coordinate
                else:
                    intersected_length = rect2_final - rect1_coordinate
                break
            else:
                rect1_coordinate += 1
        # return the values, check to make sure an overlap found
        if intersected_length == 0:
            rect1_coordinate = None
        return rect1_coordinate, intersected_length

    # putting it all together - X-axis overlap
    x_overlap_start, x_overlap_length = find_axis_overlap('x')
    y_overlap_start, y_overlap_length = find_axis_overlap('y')
    # build the dictionary
    return {
        'left_x': x_overlap_start,
        'bottom_y': y_overlap_start,
        'width': x_overlap_length,
        'height': y_overlap_length
    }
