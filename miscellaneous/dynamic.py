def trib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return trib(n - 1) + trib(n - 2) + trib(n - 3)


def make_trib_table(n):
    trib_table = [0 for n in range(n + 1)]
    trib_table[1] = trib_table[2] = 1

    for i in range(3, n + 1):
        trib_table[i] = trib_table[i - 1] + trib_table[i - 2] + trib_table[i - 3]

    return trib_table[n]


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


def lcs(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    elif strA[-1] == strB[-1]:
        # if the last characters match
        return 1 + lcs(strA[:-1], strB[:-1])
    else:
        # if the last characters don't match
        return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))


def memoize_lcs(f):
    memo = {}

    def helper(x, y):
        if (x, y) not in memo:
            memo[x, y] = f(x, y)
        return memo[x, y]

    return helper


def make_lcs_table(x, y):
    lcs_table = {}
    lcs_table[""] = 0
    # 'str' --> set(all possible )


if __name__ == "__main__":
    """print(trib(15))
    print(make_trib_table(15))

    trib = memoize(trib)
    print(trib(150))"""
    lcs = memoize_lcs(lcs)
