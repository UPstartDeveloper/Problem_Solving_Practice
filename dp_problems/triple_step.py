#!/usr/bin/env python3

"""
Cracking the Coding Interview:
8.1 Triple Step: A child is running up a staircase with n steps and can hop either 
1 step, 
2 steps, or 
3 steps at a time. 

Implement a method to count how many possible ways the child can run up the stairs.

5 --> 1,1,1,1,1,
      1,2,1,1
      1, 1, 2, 1
      1, 1, 1, 2
      1, 2, 2,
      1,2,2
      2,1,2,
      2,2,1
      1,1,3
      1,3,1
      3,1,1,
      2,3,
      3,2

Does order in which steps are taken matter? yes
n >= 1
what if n = 0? return 1

I'mma be honest, I've solved a problem very similar to this, except that 
it said that the child can only go up by 1 or 2 steps at a time. 
Do you still want me to solve this problem, and if so is it ok if I 
work off my knowledge from that problem?

Idea #1: Bottom Up DP

Let's make a table of some sample inputs/outputs:

n   |   ans
0       1
1       1
2       2 [[1, 1], [2]]
3       4 [1, 1, ,1], [2, 1], [1, 2], [3]]
4       7 [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2], [1,3], [3,1]
5       13

What pattern does this show us?
Inputs of 0, 1, and 2 are all base cases. After that (n > 2), the answer
for f(n) is just the sum of f(n - 3) + f(n - 2) + f(n - 1)

Why?
The amt of ways we can get to n steps (when taking 1 step at a time), is just
the same number of ways we get to n-1 steps, (only difference is we add 1).

Same thing when step_size is 2 - find all the ways to get to n - 2 steps, and 
add to our sum.

"""


def triple_step(steps):
    # Base Cases: init a list to store the amt of ways to the top of stairs
    num_paths = [1, 1, 2]

    # Recursive Case: find the num of ways to climb the given number of steps
    if steps > 2:
        for num_steps in range(3, steps + 1):
            # compute the answer for this subproblem
            num_ways_to_top = (
                num_paths[num_steps - 3]
                + num_paths[num_steps - 2]
                + num_paths[num_steps - 1]
            )
            # add this answer to the dp table
            num_paths.append(num_ways_to_top)
    # return the answer
    return num_paths[steps]


if __name__ == "__main__":
    # does this algorithm work w/ larger inputs
    steps = 5
    assert triple_step(5) == 13, f"Function returned {triple_step(5)} instead"

    # Time: O(n)
    # Space: O(n)
