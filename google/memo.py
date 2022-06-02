class memoize:
    """class-based way to do memoization"""

    def __init__(self, func):
        self.cache = dict()
        self.f = func

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.f(args)
        return self.cache[args]


"""func-based way"""


def memoize(func):
    cache = dict()

    def caller(*args):
        if args not in cache:
            cache[args] = func(args)
        return cache[args]

    return caller
