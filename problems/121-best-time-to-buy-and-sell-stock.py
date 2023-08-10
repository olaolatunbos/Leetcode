class Solution:
    def maxProfit(self, prices) -> int:
        buy, sell = 0, 1
        profit = 0

        while sell < len(prices):
            difference = prices[sell] - prices[buy]
            if difference < 0:
                buy = sell
            else:
                profit = max(profit, prices[sell] - prices[buy])
            sell += 1
        return profit


        