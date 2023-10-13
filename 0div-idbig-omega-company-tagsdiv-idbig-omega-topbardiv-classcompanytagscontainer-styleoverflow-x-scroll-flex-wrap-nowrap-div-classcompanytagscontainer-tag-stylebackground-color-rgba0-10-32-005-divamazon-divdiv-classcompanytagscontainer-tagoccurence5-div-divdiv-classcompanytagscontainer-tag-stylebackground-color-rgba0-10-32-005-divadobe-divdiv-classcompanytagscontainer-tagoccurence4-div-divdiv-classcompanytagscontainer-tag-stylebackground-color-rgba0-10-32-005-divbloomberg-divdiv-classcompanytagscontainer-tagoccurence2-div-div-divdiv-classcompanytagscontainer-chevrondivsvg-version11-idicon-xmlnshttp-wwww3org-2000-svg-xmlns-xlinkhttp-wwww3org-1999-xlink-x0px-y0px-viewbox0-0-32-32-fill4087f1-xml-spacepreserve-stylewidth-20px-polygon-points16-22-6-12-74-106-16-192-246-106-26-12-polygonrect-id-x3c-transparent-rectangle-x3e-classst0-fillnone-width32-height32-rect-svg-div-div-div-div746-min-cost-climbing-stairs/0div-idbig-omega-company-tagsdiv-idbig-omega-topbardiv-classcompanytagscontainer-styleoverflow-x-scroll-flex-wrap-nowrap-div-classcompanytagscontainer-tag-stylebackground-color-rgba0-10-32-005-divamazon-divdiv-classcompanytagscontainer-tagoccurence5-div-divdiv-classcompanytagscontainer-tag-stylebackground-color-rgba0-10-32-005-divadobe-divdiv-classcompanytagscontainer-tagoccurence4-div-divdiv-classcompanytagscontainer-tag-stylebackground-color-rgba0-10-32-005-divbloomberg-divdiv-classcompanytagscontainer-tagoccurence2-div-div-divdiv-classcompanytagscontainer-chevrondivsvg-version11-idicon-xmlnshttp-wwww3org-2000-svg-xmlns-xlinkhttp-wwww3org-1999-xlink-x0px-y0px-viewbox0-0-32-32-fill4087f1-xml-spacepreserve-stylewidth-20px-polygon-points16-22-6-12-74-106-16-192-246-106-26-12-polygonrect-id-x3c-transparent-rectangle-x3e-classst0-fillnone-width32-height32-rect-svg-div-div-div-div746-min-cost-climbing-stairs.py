class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @cache
        def recur(idx):
            if idx >=n:
                return 0
            
            ans =int(1e19)
            ans = min(ans,recur(idx+1)+cost[idx])
            ans = min(ans,recur(idx+2)+cost[idx])
            return ans
        
        val = min(recur(0),recur(1))
        return val