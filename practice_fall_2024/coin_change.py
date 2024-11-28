class Solution:
    """https://neetcode.io/problems/coin-change"""
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Inputs:
            coins: list[int] - types of coin vals
                immutable
                non-empty, pretty small
                sorted? - yes
                distinct? - yes
                pos - yes

            amt - non neg int

        Outputs
            int: fewest amt of coins possible to pay amt, if possible
            or -1

        EC:
            amt = 0 ---> return 0

        Intuition
            DP

        BCR:
            depends on the call graph???

        Approaches:
            let c = # of ints in coins
            let a = amt

            1) Top-Down (+ Optional Memoization) -->
                idea:
                    - backtrack to find all the possible coin combos
                    - return the one with the lowest amt of coins

                global problem
                    min_coins = init at -1

                recursive sub problem
                    inputs:
                        - amt_so_far --> init @ 0
                        - coins_used_so_far --> init @ 0
                        - coins --> given by caller

                    base cases:
                        - amt_so_far == amt
                            update min_coins w/ coins_used_so_far if appropiate
                        - amt_so_far > amt
                            return
                    recursive case
                        - amt_so_far < amt
                            coins_used_so_far += 1
                            recurse on amt_so_far + each type of coin

                Complexity (w/o memoization)
                    time: O(c ** a)
                    space: O(a)

                - how to memoize? TBD

                0
                1            5   10
                2      6  11
                3.  7


            2) Bottom Up DP

            3) Greedy -
                x1 * c1 + x2 * c2 + ... = amt

                let xs = (x1, x2, ..., xn)
                    goal: find min(sum(xs)),
                        for all xs that enable us to get
                        x1 * c1 + x2 * c2 + ... = amt

                insight:
                    addition + multiplication are commutative
                        so it's ok to be greedy

                Approach:

                    globally:
                        min_coins_possible = float("inf")

                    START
                        traverse coins in reverse
                            coins_used = 0
                            amt_left = amount

                            current_coin_type = current_pos in list
                            coef_of_current_coin = amt_left // current_coin_type
                            update amt_left --> subtract by current_coin_type * coef_of_current_coin
                            coins_used += coef_of_current_coin


                ...


        """
        ### bottom up approach - DP

        num_coins_per_amount = [-1 for _ in range(amount + 1)]
        coin_types = set(coins)
        # fill in base cases
        num_coins_per_amount[0] = 0
        for coin_type in coin_types:
            if -1 < coin_type < len(num_coins_per_amount):
                num_coins_per_amount[coin_type] = 1

        # fill in rest
        for amount in range(1, len(num_coins_per_amount)):
            # skip base cases
            if amount not in coin_types:
                min_possible_num_coins = float("inf")
                for coin in coin_types:
                    coins_used = float("inf")
                    amount_left = amount - coin
                    if -1 < amount_left < amount:
                        if num_coins_per_amount[amount_left] > -1:
                            coins_used = 1 + num_coins_per_amount[amount_left]
                    else:
                        pass

                    min_possible_num_coins = min(min_possible_num_coins, coins_used)

                if min_possible_num_coins < float("inf"):
                    num_coins_per_amount[amount] = min_possible_num_coins


        # return answer
        return num_coins_per_amount[amount]
