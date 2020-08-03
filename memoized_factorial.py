def fast_trailing_zero_factorial(n):
    fact = factorial(n)
    zeroes = count_trailing_zeroes(fact)
    return zeroes
  
def factorial(n):
    # compute the factorial
    if n == 0 or n == 1:
      return 1
    elif n > 1:
      return n * factorial(n - 1)
    
# memoize the function
def memoize(func):
    # init a cache for previous values
    num_fact = dict()
    def return_zeroes(input_num):
        # compute the factorial 
        if input_num not in num_fact:
            fact_val = func(input_num)
            # add to the dictionary
            num_fact[input_num] = fact_val
        return num_fact[input_num]
    # return the function to index the cache
    return return_zeroes

def count_trailing_zeroes(factorial):
    """Third wrapper function to count trailing zeroes of the factorial function."""
    # return the value in the cache
    factorial = str(factorial)
    index = len(factorial) - 1
    # count of number of trailing zeroes
    trailing = 0
    while index > 0:
        if factorial[index] == '0':
            trailing += 1
            index -= 1
        else:
            # time to break out of the loop
            index = 0
    return trailing


if __name__ == '__main__':
    factorial = memoize(factorial)
    print("Enter number")
    try: 
        n = int(input())
        print("The number of trailing zeroes is " + str(fast_trailing_zero_factorial(n)))
    except EOFError:
        print(end='')
 