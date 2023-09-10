class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
        n=len(jobs)
        jobs.sort(reverse=True)
        
        def recur(idx,mid):
            if idx>=n:
                return True
            
            curr = jobs[idx]
            
            for i in range(len(vec)):
                if vec[i]+curr<=mid:
                    vec[i]+=curr
                    if recur(idx+1,mid):
                        return True
                    vec[i]-=curr
                
                if vec[i]==0:
                    break
            return False
                    
                    
            
        
        
        l=max(jobs)
        r=sum(jobs)
        
        while l<=r:
            mid = (l+r)//2
            vec = [0]*(k)
            if recur(0,mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        
        return ans
                