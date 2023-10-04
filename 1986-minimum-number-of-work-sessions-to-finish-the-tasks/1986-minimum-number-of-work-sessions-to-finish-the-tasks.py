class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n =len(tasks)
        inf = int(1e19)
        maxi = max(tasks)
        ## 2^n*n*sessionTime
        dp = [[-1]*((1<<n)+10) for _ in range(maxi*n)]
        
        def recur(curr,mask):
            if mask==((1<<n)-1):
                return 0
            if dp[curr][mask]!=-1:
                return dp[curr][mask]
            ans = inf
            
            for i in range(n):
                if mask&(1<<i)==0:
                    if curr+tasks[i]<=sessionTime:
                        ans = min(ans,recur(curr+tasks[i],mask^(1<<i)))
                    else:
                        ans = min(ans,1+recur(tasks[i],mask^(1<<i)))
            dp[curr][mask] = ans
            return dp[curr][mask]
        
        val = recur(0,0)
        return val+1