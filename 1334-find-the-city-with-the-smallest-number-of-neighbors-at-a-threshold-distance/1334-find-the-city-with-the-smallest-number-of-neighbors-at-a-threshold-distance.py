'''
distance is atmost *distanceThreshold* (<=)
'''

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
 
        inf=int(1e19)
        dist= [[inf]*(n) for _ in range(n)]
        for x,y,w in edges:
            dist[x][y]=w
            dist[y][x] =w
        for i in range(n):
            dist[i][i]=0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
        
        ans =-1
        mini = int(1e19)
        for i in range(n):
            arr = dist[i]
            cnt =0 
            for j in range(n):
                if arr[j]<=distanceThreshold:
                    cnt+=1
            if cnt<=mini:
                mini=cnt
                ans=i
        return ans