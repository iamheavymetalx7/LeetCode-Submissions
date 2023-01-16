class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    
        intervals.sort(key=lambda x:x[0])
        
        ans=[]
        
        for x_,y_ in intervals:
            if ans and ans[-1][-1]>=x_:
                ans[-1][-1]=max(ans[-1][-1],y_)
            else:
                ans.append([x_,y_])
                
        return ans