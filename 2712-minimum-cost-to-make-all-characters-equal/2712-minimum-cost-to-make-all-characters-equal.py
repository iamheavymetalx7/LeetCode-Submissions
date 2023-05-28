class Solution:
    def minimumCost(self, s: str) -> int:
        cost=0
        n=len(s)
        for i in range(1,n):
            if s[i]!=s[i-1]:
                cost+=min(i, n-i)
        
        return cost
        