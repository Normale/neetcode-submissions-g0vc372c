class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        min_left = prices[left]
        max_profit = 0
        while left < len(prices)-1:
            left += 1
            profit = prices[left] - min_left
            if profit > max_profit:
                max_profit = profit
            if min_left > prices[left] :
                min_left = prices[left]
            
        return max_profit