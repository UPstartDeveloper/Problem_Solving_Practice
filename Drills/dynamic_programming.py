"""Drill class-based and function-based ways to do dynamic programming."""


class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = dict()

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]


"""
Top Down Dynamic Programming - 
both of the following approaches are great under the following conditions:
- if you already have a naive recursive solution,
the benefits:
- you can generalize these to any recursive function, 
- you don't need to change that function itself, just tweak its usage
"""


@Memoize
def fib(n):
    """Returns the nth Fibonacci number."""
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


"""Functional Approach"""


def memoize(func):
    cache = dict()

    def helper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return helper


# remember to actually APPLY the memoization function!
fib_functional = memoize(fib)


"""Bottom Up Dynamic Programming:
- better for optimizing space usage
- can be better for trickier problems - start w/ base cases and build
"""


def fib_bottom_up(n):
    """Clarify w/ interviewier, if client requests 1st Fib num,
    will they input n = 0 or n = 1?

    Assumption: they input n = 1 --> 0 is an invalid input
    """
    dp_table = [1, 1]
    # the indices of the array = sequence value of the Fibonacci number
    for input in range(2, n):
        dp_table.append(dp_table[input - 1] + dp_table[input - 2])
    return dp_table[n - 1]


if __name__ == "__main__":
    nums = [1, 10, 100, 1_000, 10_000]
    # alt way to memoize using the class based approach, no decorator
    fib_class_based = Memoize(fib)
    for n in nums:
        # --> top down can be slow if you still use recursion
        # assert fib_class_based(n) == fib_functional(n)
        print(fib_bottom_up(n))
