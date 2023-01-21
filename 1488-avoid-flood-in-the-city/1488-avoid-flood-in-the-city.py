import bisect
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        filled={}
        dryDay=[]
        n=len(rains)
        ans=[1]*n
        
        
        for day,lake in enumerate(rains):
            if not lake:
                dryDay.append(day)
                continue
            
            ans[day]=-1
            
            if lake in filled:
                if len(dryDay)==0:
                    return []
                dryDay_index = bisect.bisect_left(dryDay,filled[lake])
                if dryDay_index>=len(dryDay):
                    return []
                dryonDay = dryDay.pop(dryDay_index)
                ans[dryonDay]=lake
            filled[lake]=day
            
        return ans
                
                
                