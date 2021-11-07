def check_window(window):
    first, second, third = window
    print(first, second, third)
    if first <= second >= third or first >= second <= third:
        return False  # no switch needed
    return True  # switch needed, window is not a wave yet


def switch_order(window, switch_first_two):
    first, second, third = window
    new_order = list()
    # make a left switch
    if switch_first_two == 0:
        new_order = [second, first, third]
    else:
        new_order = [first, third, second]
    return new_order


def wave_array(integers):
    # A: sort the array
    integers.sort()
    # alternate switching first two and last two
    switch_first_two = 0  # zero = True, 1 means False
    # set indicies for overall progress
    end_overall = 3
    # iterate
    while end_overall <= len(integers):
        # check that each window is valid before moving on to the next
        start, end = 0, 2
        while end < end_overall:
            # index the window
            window = integers[start : end + 1]
            print(start, end, window)
            # check the window is a valid wave, or switch
            make_switch = check_window(window)
            print(make_switch)
            if make_switch is True:
                # get the new order
                new_order = switch_order(window, switch_first_two)
                # change it in the original array
                integers[start : end + 1] = new_order
                switch_first_two ^= 1
            # move on to next window
            print(integers)
            start += 1
            end += 1
        end_overall += 1
    return integers


if __name__ == "__main__":
    print(wave_array([1, 2, 3, 4]))
