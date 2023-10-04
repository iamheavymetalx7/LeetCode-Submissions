class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n =len(tasks)
        inf = int(1e19)
        
        ## 2^n*n*sessionTime
        
        @cache
        def recur(curr,mask):
            if mask==((1<<n)-1):
                return 0
            
            ans = inf
            
            for i in range(n):
                if mask&(1<<i)==0:
                    if curr+tasks[i]<=sessionTime:
                        ans = min(ans,recur(curr+tasks[i],mask^(1<<i)))
                    else:
                        ans = min(ans,1+recur(tasks[i],mask^(1<<i)))
            return ans
        val = recur(0,0)
        return val+1