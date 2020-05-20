"""
Hacker Rank Problem found here:
https://www.hackerrank.com/challenges/electronics-shop/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

1. Clarifying Questions
    - are the prices on positive integers?
    - will the prices alwas be unique within one array?
    - is the array sorted?
    - size limits on any kind on the lists?

2. Assumptions:
    - a keyboard and a USB always have a price > 0
    - prices are always positive integers
    - no duplicates within the same list of a product's prices
    - not sorted (although it make sense for a store)
    - from the problem description, we know the lists may or may not be equal
       in length, and that there'll always be between 1 and 1000 items for
       both a USB or keyboard (referred tp here as 'products')


Idea 1: using for loops
- esstenially re-implement naive two sum
- use for loops to record all combinations
- take the max of these combinations that is <= budget, and return it
- if all combos are > budget, then return -1
"""


def get_money_spent(keyboards, drives, b):
    # calculate all ways the customer can purchase the product
    max_combo = 0
    for k_price in keyboards:
        for d_price in drives:
            combo = k_price + d_price
            # only add combos within budget, and that have both products
            if combo <= b and k_price > 0 and d_price > 0:
                if combo > max_combo:
                    max_combo = combo
    # check to make sure a max_combo was able to be found
    if max_combo == 0:
        max_combo = -1
    return max_combo


"""
Big O Complexity:

Time: The runtime of this function rises asymptotically with respect to the
      sizes of both keyboards and drives. Since we have defined the process
      to finding all combinations of the prices using nested for loops, the
      average case runtime of this function will be O(n * m).

Space: This functions uses only local variables, so its memory usages is
       independent of the input. It is therefore O(1).

"""
