def find_busiest_period(data):
    """
    [ [1487799425, 14, 1],
        [1487799425, 4,  0],
        [1487799425, 2,  0],
        [1487800378, 10, 1],
        [1487801478, 18, 0],
        [1487801478, 18, 1],
        [1487901013, 1,  0],
        [1487901211, 7,  1],
        [1487901211, 7,  0] ]

        - multiple data points can have the same time
        - return the time of one of the data points

        - choices for the solution - one of the times

        - is the input mutable? no
        - "busiest" - most people in the mall? yes

        Idea 1: create a time distribution

        map each time --> number of people
        - so the time people enter - do those people count as "being in the mall" at
        that second, or the one after? yes

        - so the time people exit - do those people count as "being in the mall" at
        that second, or the one before? no

        - what if more than one time share the highest pop>

    time_total_pop =
    {
        1487799425: 8
        1487800378, 18
    }

    total_people = 18

    - can the total number of people ever go negative? no
        - can we assume the first point is people entering (opening time)? yes
    - allowed to use built-in sorting methods?

    """
    # A: iterate over rest of points
    pt_idx = 0
    max_pop, max_time = 0, 0
    current_pop = max_pop
    while pt_idx < len(data):
        # find the time of the poinr
        people_time = 0
        time, people, increase = data[pt_idx]
        if increase == 1:
            people_time += people
        else:
            people_time -= people
        # find the total number of people in the mall at the time
        while pt_idx < len(data) - 1 and data[pt_idx + 1][0] == time:
            pt_idx += 1
            time, people, increase = data[pt_idx]
            if increase == 1:
                people_time += people
            else:
                people_time -= people
        pt_idx += 1
        # update the current total
        current_pop += people_time
        # if the current total > largest ever
        if current_pop > max_pop:
            # updates largest popuation and corresponding time
            max_pop = current_pop
            max_time = time
    # C: return the largest time
    return max_time


"""
    # init the total population
    initial = data[0]
    total = initial[1]
    # init dict of time --> total people
    time_population = {
        initial[0]: total
    }
    # iterate over the times
    if len(data) > 1:
        for data_idx in range(1, len(data)):  # n iterations, where n = # data points
            # update the total population
            pt = data[data_idx]
            time, people, increase = pt
            if increase == 1:
                total += people
                # time_population[time] = total 
            else:  # people left the mall
                # time_population[time] = total 
                total -= people
            # update the time that has these people
            time_population[time] = total  
    # find the time w/ the most total people in mall
    times_populations = list(time_population.items())  # n
    # sort by the times
    times_populations.sort()
    # find the largest popuation
    max_pop = 0
    for index, time_pt in enumerate(times_populations):
        time, pop = time_pt
        if pop > max_pop:
            max_pop = pop
    # find the largest time w/ that population
    for index, time_pt in enumerate(times_populations):
        time, pop = time_pt
        if pop == max_pop:
            return time

"""
"""
total = 17

pt = 1487901211, 7,  0] 

{
1487799425: 8
1487800378: 18
1487901013: 17
1487901211: 17
}

Time: O(n)
Space: O(n)



[[1487799425,14,1],
[1487799425,4,0],
[1487799425,2,0],
[1487800378,10,1],
[1487801478,18,0],
[1487801478,18,1],
[1487901013,1,0],
[1487901211,7,1],
[1487901211,7,0]]


"""
