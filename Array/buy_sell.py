"""You are given an array prices where prices[i] is the price of a given stock on the ith day.
Choose a day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""
from typing import List


class Solution:
    # Memory O(1), Time O(N)
    def max_profit(self, prices: List[int]) -> int:
        lowest = float('inf')
        profit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            elif (price - lowest) > profit:
                profit = price - lowest
            # profit = max(profit, (price - lowest))
        return profit


if __name__ == "__main__":
    so = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(so.max_profit(prices))

