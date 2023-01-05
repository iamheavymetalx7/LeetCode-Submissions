class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0:
            return 0
        
        
        points.sort(key=lambda p: p[1])
    
        
        curr=points[0]
        
        arrow=1
        
        for balloon in points:
            if curr[1]<balloon[0]:
                curr= balloon
                arrow+=1
                
        return(arrow)
    
    
'''
## My solution:


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()        
        n=len(points)
        seen=set()
        
        cnt=0
        for i in range(len(points)):
            if i not in seen:
                seen.add(i)
                
                start=points[i][0]
                end=points[i][1]
                for j in range(i+1, len(points)):
                    if points[j][0]>=start and (points[j][0]<=end or points[j][1]<=start):
                        seen.add(j)
                        start=max(points[j][0],start)
                        end=min(points[j][1], end)
                    else:
                        break   
                cnt+=1
        return cnt

'''
    
                    
                        