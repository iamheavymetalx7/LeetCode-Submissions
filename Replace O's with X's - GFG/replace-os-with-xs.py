#User function Template for python3

class Solution:
    def fill(self, n, m, mat):
        # code here
        def dfs(r,c):
            vis[r][c]=1
            
            for x,y in dire:
                nr = r+x
                nc= c+y
                
                if 0<=nr<n and 0<=nc<m and not vis[nr][nc] and mat[nr][nc]=="O":
                    dfs(nr,nc)
            
        
        dire = [(1,0),(-1,0),(0,-1),(0,1)]
        vis=[[0]*m for _ in range(n)]

        for j in range(m):
            if not vis[0][j] and mat[0][j]=='O':
                dfs(0,j)
                
            if not vis[n-1][j] and mat[n-1][j]=='O':
                dfs(n-1,j)

        for i in range(n):
            if not vis[i][0] and mat[i][0]=='O':
                dfs(i,0)
                
            if not vis[i][m-1] and mat[i][m-1]=='O':
                dfs(i,m-1)
        
        
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and mat[i][j]=="O":
                    mat[i][j]="X"
        
        return mat
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends