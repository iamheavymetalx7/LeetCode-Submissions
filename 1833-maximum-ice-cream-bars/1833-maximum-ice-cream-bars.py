class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n=len(costs)
        index=0
        cnt=0
        while index<n and coins>0:
            if costs[index]<=coins:
                coins-=costs[index]
                index+=1
                cnt+=1
            else:
                break
                
        return cnt