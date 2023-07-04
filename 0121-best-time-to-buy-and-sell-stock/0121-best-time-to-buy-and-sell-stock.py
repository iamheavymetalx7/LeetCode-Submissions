class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buyprice =prices[0]
        maxProfit=0
        for price in prices:
            buyprice=min(price,buyprice)
            maxProfit = max(maxProfit, price-buyprice)
        
        return maxProfit
        