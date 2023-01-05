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
                    
                    