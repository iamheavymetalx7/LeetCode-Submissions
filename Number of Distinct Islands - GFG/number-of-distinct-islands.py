#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self,grid,vis,i,j,direction):
        n=len(grid)
        m=len(grid[0])
        
        if i<0 or i>=n or j<0 or j>=m:
            return ""
            
        if grid[i][j]==0 or vis[i][j]:
            return ""
        
        vis[i][j]=True
        
        traversal=direction
        
        traversal+=self.dfs(grid,vis,i+1,j,"D")
        traversal+=self.dfs(grid,vis,i-1,j,"U")
        traversal+=self.dfs(grid,vis,i,j+1,"R")
        traversal+=self.dfs(grid,vis,i,j-1,"L")
        
        traversal+="B"
        
        return traversal
        
    
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        n = len(grid)
        m = len(grid[0])
        vis=[[False]*m for j in range(n)]
        islandSet = set()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not vis[i][j]:
                    path = self.dfs(grid,vis,i,j,"O")
                    islandSet.add(path)
        # print(islandSet)
        return len(islandSet)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends