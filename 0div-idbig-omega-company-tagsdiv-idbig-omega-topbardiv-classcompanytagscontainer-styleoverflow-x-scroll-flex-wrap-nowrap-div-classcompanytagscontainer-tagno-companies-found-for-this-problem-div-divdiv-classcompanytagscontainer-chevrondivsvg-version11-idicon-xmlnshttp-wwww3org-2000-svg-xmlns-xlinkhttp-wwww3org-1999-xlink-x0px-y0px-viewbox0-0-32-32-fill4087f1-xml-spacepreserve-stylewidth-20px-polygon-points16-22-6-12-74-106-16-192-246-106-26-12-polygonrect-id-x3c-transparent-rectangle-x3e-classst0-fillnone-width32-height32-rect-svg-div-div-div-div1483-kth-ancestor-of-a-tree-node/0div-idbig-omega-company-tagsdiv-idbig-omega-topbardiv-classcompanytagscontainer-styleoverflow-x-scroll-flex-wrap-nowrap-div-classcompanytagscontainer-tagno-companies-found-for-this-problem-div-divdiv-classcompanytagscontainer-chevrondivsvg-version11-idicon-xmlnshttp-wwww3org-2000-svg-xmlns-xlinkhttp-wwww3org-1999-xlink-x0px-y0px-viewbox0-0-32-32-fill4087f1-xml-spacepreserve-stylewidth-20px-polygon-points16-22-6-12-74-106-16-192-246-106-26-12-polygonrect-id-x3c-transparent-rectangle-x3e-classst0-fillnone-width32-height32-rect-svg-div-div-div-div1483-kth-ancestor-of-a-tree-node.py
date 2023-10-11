class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        m = 1+int(log2(n))

        self.dp = [[-1]*(m) for _ in range(n)]
        
        for i in range(n):
            self.dp[i][0]=parent[i]
            
        for j in range(1,m):
            for i in range(n):
                if self.dp[i][j-1]!=-1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
                else:
                    self.dp[i][j]=-1
        
        
        
        
    def getKthAncestor(self, node: int, k: int) -> int:
                    
        while k and node!=-1:
            i = int(log2(k))
            node = self.dp[node][i]
            k-=(1<<i)
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)