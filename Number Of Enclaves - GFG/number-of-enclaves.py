#User function Template for python3

from typing import List
from collections import deque
class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        n=len(grid)
        m=len(grid[0])
        dire= [(1,0),(0,1),(0,-1),(-1,0)]
        q=deque()
        
        vis=[[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if (i==0 or i==n-1 or j==0 or j==m-1):
                    if grid[i][j]:
                        q.append([i,j])
                        vis[i][j]=1
                        
        while q:
            r,c=q.popleft()
            
            for x,y in dire:
                nr = r+x
                nc =c+y
                
                if 0<=nr<n and 0<=nc<m and not vis[nr][nc] and grid[nr][nc]:
                    q.append([nr,nc])
                    vis[nr][nc]=1
        
        cnt=0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not vis[i][j]:
                    cnt+=1
                    
        return cnt
            
            

        

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends