from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

        Input/Problem:
            non empty int arr
            non neg
            dupes are poss
            immutable

            buy/sell multiple times ----> global total, max profit
            CAN buy/sell same day

        Intution:
            dynamic programming ----> solution
            heap - 2nd

        EC:
            1) empty arr ----> N/A
            2) neg prices ---> N/A
            3) all same ---> return 0 -- [7, 7, 7, 7]
            4) decreasing/increasing ----

        Test Cases:

          [7,1,5,3,6,4] ----> output 7
          [1,2,3,4,5] ------> output 4
          [7,6,4,3,1] ------> output 0

        Approach:

            1. Stepping Stone Problem

                BTBS I -- only buy and sell one time

                [7,1,5,3,6,4]
                 ^
                 A: init max_profit, current_stock_held
                 B: each iter:
                    - best to buy? (meaning, is it the lowest we've seen?)
                        - current_stock_held = prices[i]
                    - OR best time to sell? (prices[i] - current_stock_held > max_profit?)
                        - max_profit = prices[i] - current_stock_held

                BTBS II -- buy and sell multiple time

                [7,1,5,3,6,4]
                 ^
                 A: init max_profit, current_stock_held
                 B: each iter:
                    - best to buy? (meaning, is it the lowest we've seen?)
                        - current_stock_held = prices[i]
                    - OR best time to sell? (prices[i] - current_stock_held > max_profit?)
                        - max_profit += prices[i] - current_stock_held


                [7,1,5,2,5,4]
                   B ^ ^
                     S S S.S
                choosing a time to sell:
                    - max(profiy on transaction) AND
                    - min(index of sell price)

                A: init max_profit, current_stock_held
                B: for loop
                    - best to buy? (meaning, is it the lowest we've seen?)
                        - current_stock_held = prices[i]
                        - OR best time to sell? (prices[i] - current_stock_held > max_profit?)
                            - max_profit += prices[i] - current_stock_held


                [7,1,5,3,6,4]
                 ^

                lowest_price = 7


        """
        ### Big O: O(n) time and O(1) space
        # A: init the output and iterator
        total, index = 0, 0
        # B: sum the profits from each "best" transaction
        while index < len(prices):
            # a) look for a surge in prices
            valley, peak = index, index + 1
            # b) only accept increasing/stable prices in this range
            while peak < len(prices) and prices[peak] >= prices[peak - 1]:
                peak += 1
            # c) add to the profits
            total += prices[peak - 1] - prices[valley]
            # d) move on to the next transaction
            index = peak
        # C: all done! return the total
        return total
