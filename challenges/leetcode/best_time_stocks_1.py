"""
121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element
is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
import math
import unittest


def best_time_stocks_1(prices):
    if len(prices) < 0:
        return 0

    lowest_price = math.inf
    max_profit = 0
    for i in range(len(prices)):
        lowest_price = min(lowest_price, prices[i])
        profit = prices[i] - lowest_price
        max_profit = max(max_profit, profit)

    return max_profit


class TestBestTimeStocks1(unittest.TestCase):
    def test_best_time_stocks_1_single(self):
        self.assertEqual(0, best_time_stocks_1([1]))

    def test_best_time_stocks_1_leetcode1(self):
        self.assertEqual(5, best_time_stocks_1([7, 1, 5, 3, 6, 4]))
