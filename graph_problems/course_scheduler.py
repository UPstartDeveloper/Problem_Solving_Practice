def can_finish(num_courses, prerequisites):
    # build an adjacency matrix of the courses
    course_sequences = {course: set() for course in range(num_courses)}
    # add the links from courses to their prerequisites
    for sequence in prerequisites:
        course, prerequisite = sequence
        course_sequences[prerequisite].add(course)

    """
    course_sequences = {
    0: {1},
    1: {0}
    }
    """
    # detect cycles using DFS
    # A: initialize a stack to map out your courses
    course_load = list()
    # B: find a course with no prerequisites (push onto the stack)
    for course in course_sequences:
        if len(course_sequences[course]) == 0:
            course_load.append(course)
            break
    # no courses could be taken - not possible
    else:
        return False
    # C: track the courses you've taken
    courses_taken = set()
    # while stack has elements
    while course_load:
        # pop from the stack
        course = course_load.pop()
        # check if it's not already in the path - if it is, we have a cycle
        if course in courses_taken:
            return False
        else:
            courses_taken.add(course)
        # push all it's next courses onto the stack
        for next_course in course_sequences[course]:
            if next_course not in courses_taken:
                course_load.append(next_course)
    # courses taken, and no cycles  - possible
    return True
