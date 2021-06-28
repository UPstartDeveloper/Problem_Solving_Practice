def fib(x):
    if x == 1 or x == 0:
        return x
    else:
        return fib(x - 1) + fib(x - 2)


class Memoize:
    def __init__(self, func):
        self.function = func
        self.cache = dict()

    def __call__(self, args):
        if args not in self.cache:
            self.cache[args] = self.function(args)
        return self.cache[args]


def memoize(function):
    cache = dict()
    def efficient_output(args):
        if args not in cache:
            cache[args] = function(args)
        return cache[args]

    return efficient_output


memoized_fib = memoize(fib)
