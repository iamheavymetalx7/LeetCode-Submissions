class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
        
        n=len(jobs)
        jobs.sort(reverse=True)

        
        def recur(idx,val):
            if idx>=n:
                return True
            
            curr = jobs[idx]
            
            for i in range(len(vec)):
                if vec[i]+curr<=mid:
                    vec[i]+=curr
                    if recur(idx+1,val):
                        return True
                    vec[i]-=curr
                
                if vec[i]==0:
                    break
            return False
                    
            
            
        
        
        l=max(jobs)-10
        r=sum(jobs)+10
        while r>l+1:
            mid =(l+r)//2
            
            vec= [0]*(k)
            
            if recur(0,mid):
                r=mid
            else:
                l = mid
        return r