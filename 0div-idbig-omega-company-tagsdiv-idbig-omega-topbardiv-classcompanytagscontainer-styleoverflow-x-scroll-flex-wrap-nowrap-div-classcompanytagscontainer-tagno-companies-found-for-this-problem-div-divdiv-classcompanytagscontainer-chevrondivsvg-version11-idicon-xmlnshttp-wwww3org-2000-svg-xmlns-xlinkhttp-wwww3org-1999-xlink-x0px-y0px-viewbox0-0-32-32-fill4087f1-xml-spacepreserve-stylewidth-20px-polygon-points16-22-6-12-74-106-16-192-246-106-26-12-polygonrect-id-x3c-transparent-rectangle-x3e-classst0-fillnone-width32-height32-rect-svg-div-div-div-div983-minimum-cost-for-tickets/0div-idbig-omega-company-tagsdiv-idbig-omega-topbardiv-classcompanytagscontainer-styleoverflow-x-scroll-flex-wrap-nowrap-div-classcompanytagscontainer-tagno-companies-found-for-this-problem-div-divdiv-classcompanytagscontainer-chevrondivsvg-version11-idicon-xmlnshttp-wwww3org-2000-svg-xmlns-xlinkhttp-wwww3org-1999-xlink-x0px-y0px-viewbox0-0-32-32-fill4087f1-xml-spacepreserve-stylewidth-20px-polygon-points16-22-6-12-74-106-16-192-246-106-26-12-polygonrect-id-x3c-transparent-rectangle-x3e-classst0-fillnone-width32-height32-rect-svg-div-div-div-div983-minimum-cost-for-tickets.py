class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        n = len(days)
        inf = int(1e19)
        
        @cache
        def dfs(i):
            if i>=len(days):
                return 0
            
            ans = inf
            for d,c in zip([1,7,30],costs):
                val = days[i]+d
                j = bisect_left(days,val)
                ans = min(ans, c+dfs(j))
            return ans
        return dfs(0)