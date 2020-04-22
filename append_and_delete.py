'''Problem found on Hacker Rank:
    https://www.hackerrank.com/challenges/append-and-delete/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen
'''


def appendAndDelete(s, t, k):
    # make preliminary check
    if s == t:
        return 'Yes'
    # make the strings into lists, so they easier to work with
    s = list(s)
    t = list(t)
    # iterate over strings to see how much of a common prefix they share
    index = 0
    while index < len(s) and index < len(t):
        letter_s, letter_t = s[index], t[index]
        if letter_s != letter_t:
            break
        index += 1
    # delete letters in s from this index onwards
    for i in range(index, len(s)):
        if k > 0 and i < len(s):
            s[i] = ''
            # print(s, i)
            k -= 1
    # append letters to s from t, also starting at this index
    # print(f'k: {k}')
    for i in range(index, len(t)):
        if k > 0 and i < len(t):
            s.append(t[i])
            k -= 1
    # see if the strings are equal now, and make decision
    s = ''.join(s)
    t = ''.join(t)
    if s == t and k >= 0:
        return 'Yes'
    else:
        # print(f'S: {s}')
        # print(f't: {t}')
        return 'No'


if __name__ == '__main__':
    s = 'y'

    t = 'yu'

    k = 2

    result = appendAndDelete(s, t, k)
    print(result)
