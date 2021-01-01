"""
Coins: Given an infinite number of 
- quarters (25 cents), 
- dimes (10 cents), 
- nickels (5 cents), and 
- pennies (1 cent), 

write code to calculate the number of ways of representing n cents.

So for example: 

input => n = 12 
output => 1. 1x12
          2. 1x2 + 5x2
          3. 1x2 + 10x1

          ==> the output would be 3, correct?

Questions:
so n is always a nonnegative integer? yes
and we return just the number of combinations, correct?

Brainstorming:

n = 1a + 5b + 10c + 25d

and our output is basically the number of solutions to this equation

1. Backtracking 

Break down the problem a little
   0  1  2  3
- [a, b, c, d]

- Map Each index to a Multiplier
    - 0: 1
    - 1: 5
    - 2: 10
    - 3: 25

- Choices:
    a, b, c, d
- Constraints: --> n >= 1a + 5b + 10c + 25d
- Goal: --> we want to get solve n = 1a + 5b + 10c + 25d, with out any repeats

- Subproblem:
- start off with one coin (penny), and see how many of them take to meet n
    - n / 1 = # pennies (higher bound)
    - lower bound is obviously 0

- once we have that upper bound, we could decrement the number of pennies, 
    - and at each iteration see how the others could meet the n values

1       |      5       |        10       |      25      |   combination?
12             0                0               0               +1
11             0                0               0                0
10             0                0               0                0
9              0                0               0                0
8              0                0               0                0
7              1                0               0               +1
6              0                0               0                0
6              1                0               0                0
5              0                0               0                0
5              1                0               0                0
4              0                0               

as we move to each multiplier:
- if the remaining change >= the multiplier, try out coefficients from 0 --> until amt > n
- if the remaining change < the multiplier, leave a 0 there and move on 
"""


class Solution:

    next_multipliers = {
        1: 5,
        5: 10,
        10: 25,
        25: 1,
    }

    coins = list()

    def make_change(self, n: int) -> bool:
        '''returns if we have the right number of coins to make n cents.'''
        change = (
            (1 * self.coins[0]) + 
            (5 * self.coins[1]) + 
            (10 * self.coins[2]) + 
            (25 * self.coins[3])
        )
        return change == n

    """def get_coin_combinations(self, n, remainder=None, multiplier=1):
        # Base Case: init the number of combinations, and the coins array
        if remainder is None:
            remainder = n
            self.combos = 0
        # Base Case: when we have a combo, potentially
        elif remainder == 0:  # and self.make_change(n) is True:
            # we've found another combo
            self.combos += 1
            print(f"Combo found: {multiplier}")
        # Recursive Case: otherwise find the next combination
        if remainder > 0:
            # calculate the upper bound for the current multiplier
            upper = remainder // multiplier
            original_remainder = remainder
            # check that the multiplier is useful in making combos
            if upper > 0:  
                # iterate down from the upper bound
                for coefficient in range(upper, -1, -1):
                    # decrement the n (update the remainder)
                    print(f'Remainder before multiplication: {remainder, coefficient, multiplier}')
                    # new_remainder = remainder - (coefficient * multiplier)
                    remainder -= (coefficient * multiplier)
                    print(f'Remainder after multiplication: {remainder}')
                    # try to see how we can combine w/ other multipliers
                    next_multiplier = self.next_multipliers[multiplier]
                    self.get_coin_combinations(n, remainder, next_multiplier)
                    # "reset" the remainder for the next iteration
                    remainder = original_remainder
        # if we reach the end, we've gotten all combinations
        # if multiplier == 1:
        return self.combos"""

    def get_coin_combinations_brute_force(self, n):
        """
        Big O Analysis
        Time: O(n^4)
        Space: O(1)
        """
        # A: calculate the upper bounds for all the weights
        combos = 0
        one_bound = n
        five_bound = n // 5
        ten_bound = n // 10
        two_five_bound = n // 25
        # B: find all the combinations
        for one_coef in range(one_bound + 1):
            for five_coef in range(five_bound + 1):
                for ten_coef in range(ten_bound + 1):
                    for twenty_five_coef in range(two_five_bound + 1):
                        # sum the variables
                        summation = (
                            (one_coef * 1) + (five_coef * 5) +
                            (ten_coef * 10) + (twenty_five_coef * 25)
                        )
                        # see if it fits
                        if summation == n:
                            combos += 1
        # C: return the answer
        return combos

if __name__ == "__main__":
    n = 125
    sol = Solution()
    print(sol.get_coin_combinations(n))


"""






1      12      
2      12      0       5       1
1      12      12      1       0    12
sf     n       r       m       c    u
"""


