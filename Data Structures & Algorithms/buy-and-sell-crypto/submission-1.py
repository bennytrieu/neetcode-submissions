class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = profit = 0
        right = 1
        while right < len(prices):
            profit = max(profit, prices[right] - prices[left])
            right += 1
            if right == len(prices) and left != len(prices) - 1:
                left += 1
                right = left
        return profit
