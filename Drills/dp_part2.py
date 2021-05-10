class Memoize:
    '''OO way to implement top down DP.'''
    def __init__(self, func):
        self.func = func
        self.cache = dict()

    def __call__(self, args):
        if args not in self.cache:
            self.cache[args] = self.func(args)
        return self.cache[args]


# How to Apply the OO way to a function outside the class
@Memoize
def fib(num):
    '''recursive function is O(n!) w/o dp.'''
    if num == 0 or num == 1:
        return num
    elif num > 1:
        return fib(num - 1) + fib(num - 2)


def memoize(func):
    '''functional way to implement top down DP.'''
    cache = dict()

    def use_cache(args):
        if args not in cache:
            cache[args] = func(args)
        return cache[args]

    return use_cache


def factorial(num):
    '''Another recursive function'''
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


# How to Apply the Functional Approach:
factorial = memoize(factorial)




