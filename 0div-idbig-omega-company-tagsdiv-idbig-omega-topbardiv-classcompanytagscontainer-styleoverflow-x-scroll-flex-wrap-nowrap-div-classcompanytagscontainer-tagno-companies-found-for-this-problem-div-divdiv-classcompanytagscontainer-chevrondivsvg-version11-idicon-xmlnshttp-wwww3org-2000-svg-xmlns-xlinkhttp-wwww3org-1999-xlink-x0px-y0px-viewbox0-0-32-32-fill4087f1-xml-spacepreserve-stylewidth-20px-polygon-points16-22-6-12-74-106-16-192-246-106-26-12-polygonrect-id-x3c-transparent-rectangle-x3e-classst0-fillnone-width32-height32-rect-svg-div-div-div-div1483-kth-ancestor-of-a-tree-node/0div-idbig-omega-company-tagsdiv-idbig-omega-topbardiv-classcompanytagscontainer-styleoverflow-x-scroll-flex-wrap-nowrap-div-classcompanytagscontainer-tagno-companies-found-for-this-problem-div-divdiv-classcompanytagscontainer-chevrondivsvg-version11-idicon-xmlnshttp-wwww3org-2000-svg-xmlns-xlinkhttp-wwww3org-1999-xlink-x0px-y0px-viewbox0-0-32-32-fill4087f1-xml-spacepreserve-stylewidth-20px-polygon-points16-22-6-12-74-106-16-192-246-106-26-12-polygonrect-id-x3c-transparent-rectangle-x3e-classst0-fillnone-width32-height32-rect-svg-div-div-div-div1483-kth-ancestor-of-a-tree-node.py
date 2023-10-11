class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.m = 1+int(log2(n))

        self.dp = [[-1]*(self.m) for _ in range(n)]
        
        for i in range(n):
            self.dp[i][0]=parent[i]
            
        for j in range(1,self.m):
            for i in range(n):
                if self.dp[i][j-1]!=-1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
                else:
                    self.dp[i][j]=-1
        
        
        
        
    def getKthAncestor(self, node: int, k: int) -> int:
        ans = node
        
        for i in range(self.m+1):
            if k&(1<<i):
                ans = self.dp[ans][i]
                if ans==-1:
                    break
                k-=(1<<i)
        return ans
            
        

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)