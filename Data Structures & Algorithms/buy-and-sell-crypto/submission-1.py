class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        maximum_profit = 0
        for buy in range(len(prices)):
            for sell in range(buy, len(prices)):
                if prices[sell] - prices[buy] > maximum_profit:
                    maximum_profit = prices[sell] - prices[buy]
        
        return maximum_profit



        