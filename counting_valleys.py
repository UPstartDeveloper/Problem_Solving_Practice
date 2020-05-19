"""
Hacker Rank problem found on:
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

Idea #1: using a for loop
start increment a down_count once we start seeing D's
    - if we see a D, the down_count += 1
    - if we see a U, the down_count -= 1
    - if down_count == 0, then valley_count += 1

    return valley count

Idea #2: using a queue
enqueue D steps, dequeue when we see U steps, increment valley count when
the queue has a length of 0

Idea #3: using a while loop
A: traverse over the string
B: track the altitude overall
C: if we see a 'D':
    start keeping track of the steps taken in the valley
    if the valley_depth == altitude, then increment valley_count and exit the
        inner loop
D: fast forward the index by howver many steps just taken in the inner loop, or
    just by 1 if we didn't enter the loop
E: after the traversal, return the valley_count

Idea #4: using compound conditional
- assume that we only need to account for a 'U' if it's getting us out of a
  valley
- only time I need to increment valley count is after a 'U' step
"""


def counting_valleys(n, s):
    """altitude, down_count, valley_count = 0, 0, 0
    for i in range(len(s)):
        letter = s[i]
        if letter == 'U' and altitude < 0:
            altitude += 1
            # if down_count > 0:
            # down_count -= 1
        elif letter == 'D':
            # down_count += 1
            altitude -= 1
        print(altitude)
        if altitude == 0:
            valley_count += 1

    return valley_count
    steps = list()
    for i in range(len(s)):
        letter = s[i]
        if letter == 'U' and len(steps) > 0:
            steps.pop()
            # if down_count > 0:
            # down_count -= 1
        elif letter == 'D':
            # down_count += 1
            steps.append(letter)
        print(steps)
        if len(steps) == 0:
            valley_count += 1

    return valley_count
    altitude, valley_count, i = 0, 0, 0
    while i < len(s):
        letter = s[i]
        if letter == 'U':
            altitude += 1
        elif letter == 'D':
            altitude -= 1
        if altitude <= 0:
            valley_depth, j = altitude * -1, i + 1
            while j < len(s):
                letter_of_valley = s[j]
                if letter_of_valley == 'U':
                    valley_depth -= 1
                    altitude += 1
                elif letter_of_valley == 'D':
                    valley_depth += 1
                    altitude -= 1
                if valley_depth == 0:
                    valley_count += 1
                    i += j - i  # advance forward the outer loop
                    j = len(s)  # breaks the inner loop
                else:
                    j += 1
        else:
            i += 1
    return valley_count"""
    altitude, valley_depth, valley_count = 0, 0, 0
    for letter in s:
        # adjust the altitude and depth on a 'D'
        if letter == 'D':
            # entering a valley
            if altitude == 0:
                valley_depth += 1
            altitude -= 1
        # adjust the altitude and depth on a 'U'
        elif letter == 'U':
            altitude += 1
            if valley_depth > 0:
                valley_depth -= 1
            # exiting a valley
            if valley_depth == 0 and altitude == 0:
                valley_count += 1
    return valley_count
