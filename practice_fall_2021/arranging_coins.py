class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
             Leetcode: https://leetcode.com/problems/arranging-coins/
             Input/Problems:
                 n = unsigned 32-bit int > 0

                 return # of rows that are complete

                 num_coins_in_row = 1 + (num_coins_in_row - 1)

             EC:

                 1) n <= 0 --> ValueError

             Intuition:

                 1 + 2 + 3 + 4 + ... <= n

             Approach:

             1) While loop - O(n) time, O(1) space
                 n = total_supply_coins
                 A: num_rows = 0, num_coins_row = 1
                 B: add rows until coins run out (total_supply_coins > 0)
                     1) total_supply_coins -= num_coins_row  - make a new row
                         a) if total_supply_coins < 0 --> break out of loop
                     2) num_rows += 1
                     3) num_coins_row += 1
                 C: num_rows

             2)

             TSC = 5, 4, 2, -1

             NR = 0, 1, 2

             NCR = 1, 2, 3


        Row Num = i |   Total Coins
             1           1
             2           3 = row_num[i] + total_coins[i - 1]
             3           6
             4.          10

             Mathy
                 A: calculate k --> sq. root of 2n
                 B: calculate "ideal n" for k?
                 C: compare n == "ideal n"
                     return k
                    elif n < ideal n:
                     return k - 1

             n = 10 / 2 ==> 5? X

             log(base 2) (n)

        """
        # A: init values
        num_rows, num_coins_row = 0, 1  # O(1)
        # B: add rows until coins run out
        total_supply_coins = n
        while total_supply_coins > 0:  # n / 2 iteratios
            # 1) make a new row
            total_supply_coins -= num_coins_row
            # early exit
            if total_supply_coins < 0:
                break
            # move on
            num_rows += 1
            num_coins_row += 1
        # C: num_rows
        return num_rows
