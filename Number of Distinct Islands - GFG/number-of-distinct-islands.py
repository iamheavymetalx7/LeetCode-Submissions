#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self,grid,vis,i,j,direction):
        global string
        n=len(grid)
        m=len(grid[0])
        
        if i<0 or i>=n or j<0 or j>=m:
            return
            
            
        if grid[i][j]==0 or vis[i][j]:
            return

        vis[i][j]=True

        string+=direction
        


        
        self.dfs(grid,vis,i+1,j,"D")
        self.dfs(grid,vis,i-1,j,"U")
        self.dfs(grid,vis,i,j+1,"R")
        self.dfs(grid,vis,i,j-1,"L")
        
        string+="B"  ##back

        return string
        
    
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        global string
        n = len(grid)
        m = len(grid[0])
        vis=[[False]*m for j in range(n)]
        islandSet = set()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not vis[i][j]:
                    string=""
                    self.dfs(grid,vis,i,j,"O")
                    islandSet.add(string)
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