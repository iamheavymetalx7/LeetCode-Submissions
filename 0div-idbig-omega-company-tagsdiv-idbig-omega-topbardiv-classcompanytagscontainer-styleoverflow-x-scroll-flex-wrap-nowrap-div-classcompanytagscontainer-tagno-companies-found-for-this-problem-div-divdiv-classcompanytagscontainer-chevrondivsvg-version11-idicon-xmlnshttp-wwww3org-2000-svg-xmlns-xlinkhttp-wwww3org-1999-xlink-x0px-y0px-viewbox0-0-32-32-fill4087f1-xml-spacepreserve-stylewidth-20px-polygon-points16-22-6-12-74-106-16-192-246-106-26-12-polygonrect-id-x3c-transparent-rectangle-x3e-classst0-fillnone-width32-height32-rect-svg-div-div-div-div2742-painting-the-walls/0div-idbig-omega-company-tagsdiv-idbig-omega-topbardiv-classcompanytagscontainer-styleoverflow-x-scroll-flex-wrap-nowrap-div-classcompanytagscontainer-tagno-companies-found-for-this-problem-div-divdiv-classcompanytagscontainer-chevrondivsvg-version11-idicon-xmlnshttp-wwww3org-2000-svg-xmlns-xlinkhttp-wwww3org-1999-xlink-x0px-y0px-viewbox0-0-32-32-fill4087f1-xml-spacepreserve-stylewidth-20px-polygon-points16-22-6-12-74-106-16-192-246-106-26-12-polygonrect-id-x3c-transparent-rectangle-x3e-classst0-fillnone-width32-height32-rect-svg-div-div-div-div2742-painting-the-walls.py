class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        n = len(cost)
        @cache
        def recur(i,rem):
            if rem<=0:
                return 0
            if i>=n:
                return int(1e19)
            ans = int(1e19)
            ans = min(ans,cost[i]+recur(i+1,rem-1-time[i]))
            ans = min(ans,recur(i+1,rem))
            return ans
        val =recur(0,n)
        return val