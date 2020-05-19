"""
Hacker Rank problem found on:
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

Idea #1:
start increment a down_count once we start seeing D's
    - if we see a D, the down_count += 1
    - if we see a U, the down_count -= 1
    - if down_count == 0, then valley_count += 1

    return valley count

Idea #2
enqueue D steps, dequeue when we see U steps, increment valley count when
the queue has a length of 0
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

    return valley_count"""
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
