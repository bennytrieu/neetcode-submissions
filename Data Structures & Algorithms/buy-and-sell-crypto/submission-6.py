class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = profit = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                total = prices [right] - prices[left]
                profit = max(total, profit)
            else:
                left = right
            right += 1
        return profit