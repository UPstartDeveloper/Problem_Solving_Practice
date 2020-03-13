# Solving the Hacker Rank problem found here: https://www.hackerrank.com/challenges/staircase/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign


def staircase(hashtags):
    '''Given an integer number of hashtags, return a right aligned staircase of
       those characters.

    '''
    full = ""
    quota = 1
    for i in range(hashtags):
        line = ""
        for j in range(hashtags):
            if hashtags - j <= quota:
                line += "#"
            else:
                line += " "
        full += line + "\n"
        quota += 1
    return full


if __name__ == "__main__":
    print(staircase(4))
