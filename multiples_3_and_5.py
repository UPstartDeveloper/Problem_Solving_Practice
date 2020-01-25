"""
Problem Statement:

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_all_multiples(cutoff):
    """Return the answer to the answer above.

      Parameters:
      cutoff -- int: the value under which we are summing values of 3 and 5

      Return: int - sum of all multiples of 3 and 5 below cutoff.
                    Only natural numbers are included in the sum.

    """
    sum = 0
    for i in range(1, cutoff):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


if __name__ == '__main__':
    cutoff = 1000
    sum_all_multiples_3_and_5 = sum_all_multiples(cutoff)
    print(f'The sum of all the multiples of 3 or 5 below 1000: ' +
          f'{sum_all_multiples_3_and_5}')
