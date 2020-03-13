# Solving the Hacker Rank problem found here:
# https://www.hackerrank.com/challenges/staircase/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign


def staircase(num_steps):
    """Given an integer number of num_steps, return a right aligned staircase of
       those characters.

       Parameters:
       num_steps(int): a value representing the number of steps there are in
                      the staircase. This will also be the same as the number
                      of num_steps symbols on the last step (the line printed
                      last to standard output).

       Returns:
       None

    """
    # initialize a count of symbols to print on each step of the staircase
    quota = 1
    # build the string representing each step of the staircase
    for i in range(num_steps):
        line = ""
        for j in range(num_steps):
            # print spaces until it is time to add # to the output line
            if num_steps - j <= quota:
                line += "#"
            else:
                line += " "
        # display the output
        print(line)
        # increment the number of symbols needed for the next iteration
        quota += 1
    return None


if __name__ == "__main__":
    # test input of 4 steps
    staircase(4)
