class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n=len(rains)
        ans =[1 for _ in range(n)]
        filled=defaultdict(int)
        dryday=[]
        
            
        for d,l in enumerate(rains):
            if not l:
                dryday.append(d)
                continue
            
            ans[d]=-1
            
            if l in filled:
                if not dryday:
                    return []
                idx = bisect.bisect_left(dryday,filled[l])
                if idx>=len(dryday):
                    return []
                dryonDay = dryday.pop(idx)
                ans[dryonDay]=l
            filled[l] = d
        return ans
            
                
                
            
                        
            
            