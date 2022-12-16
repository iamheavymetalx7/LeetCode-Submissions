class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        profit=0
        
        for j in range(1,len(prices)):
            mini=min(mini,prices[j])
            cost = prices[j]-mini
            profit = max(profit,cost)
        return profit