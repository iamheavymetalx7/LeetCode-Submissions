class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_x,new_y = newInterval
        
        intervals.append([new_x,new_y])
            
        intervals.sort()

        ans = []
        
        for x_,y_ in intervals:
            if ans and ans[-1][-1]>=x_:
                ans[-1][-1]=max(y_, ans[-1][-1])
            else:
                ans.append([x_,y_])
                
        return ans                
                
        