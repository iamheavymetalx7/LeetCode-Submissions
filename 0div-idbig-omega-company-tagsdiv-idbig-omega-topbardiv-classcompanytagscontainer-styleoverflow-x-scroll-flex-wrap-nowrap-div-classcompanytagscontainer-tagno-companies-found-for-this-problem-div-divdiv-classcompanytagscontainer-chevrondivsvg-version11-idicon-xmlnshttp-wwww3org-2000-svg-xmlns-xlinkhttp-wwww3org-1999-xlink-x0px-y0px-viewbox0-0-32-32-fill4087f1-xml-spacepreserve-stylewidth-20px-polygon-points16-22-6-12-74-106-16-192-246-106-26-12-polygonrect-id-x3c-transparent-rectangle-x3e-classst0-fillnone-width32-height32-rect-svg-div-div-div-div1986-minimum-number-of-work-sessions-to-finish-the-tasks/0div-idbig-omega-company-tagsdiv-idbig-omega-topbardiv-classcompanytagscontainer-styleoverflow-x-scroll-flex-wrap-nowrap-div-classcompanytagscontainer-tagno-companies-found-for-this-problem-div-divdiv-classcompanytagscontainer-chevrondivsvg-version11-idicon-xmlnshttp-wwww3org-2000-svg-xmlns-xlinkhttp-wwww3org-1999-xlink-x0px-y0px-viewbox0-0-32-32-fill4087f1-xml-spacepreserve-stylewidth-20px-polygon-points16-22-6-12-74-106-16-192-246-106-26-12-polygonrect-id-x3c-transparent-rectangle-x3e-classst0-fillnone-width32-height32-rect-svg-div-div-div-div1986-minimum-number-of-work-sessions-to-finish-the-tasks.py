class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n =len(tasks)
        inf = int(1e19)
        mx = (1<<n)-1
        
        ## time complexity : 2^n * n
        @cache
        def dp(mask):
            if mask==mx:
                return (1,0)
            
            ans = (inf,inf)
            
            for j in range(n):
                if mask&(1<<j)==0:
                    pieces,last = dp(mask^(1<<j))
                    full = (last+tasks[j] > sessionTime)
                    ans = min(ans,(pieces+full, tasks[j]+(1-full)*last))
            return ans
        
        val = dp(0)
        return val[0]