from collections import defaultdict 
import math
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=2:
            return len(points)
        ans=-math.inf
        def find_slope(p1,p2):
            x1,y1=p1
            x2,y2=p2
            
            if x1==x2:
                return inf
            
            return (y2-y1)*1.0/(x2-x1)
        
        for i,point1 in enumerate(points):
            slope_dic=defaultdict(int)
            for j, point2 in enumerate(points[i+1:]):
                
                slope = find_slope(point1,point2)
                slope_dic[slope]+=1
                
                ans= max(ans, slope_dic[slope])
        return ans+1
        