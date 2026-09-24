class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        max_proff = 0
        for i in range(1,len(prices)):
            profit = prices[i]-mini
            max_proff = max(max_proff,profit)
            mini = min(mini,prices[i])
        return max_proff
        