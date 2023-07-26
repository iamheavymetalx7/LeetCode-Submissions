#User function Template for python3
class UnionFind:
    # UnionFind　初期化 使う要素の数(n)をここで宣言する。Selfというインスタンスを作って値を入れる
    def __init__(self,n):
        self.n=n
        self.parent_size=[-1]*n
 
    def leader(self,a):#グループリーダーの確認
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
 
    def merge(self,a,b):#グループの併合を要素aとbで行う
        x,y=self.leader(a),self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y]=x
        return 
 
    def same(self,a,b):#グループが同一が同かa,bで確認
        return self.leader(a) == self.leader(b)
 
    def size(self,a):#所属するグループの要素の数の確認
        return abs(self.parent_size[self.leader(a)])
 
    def groups(self):#グループ全体の確認
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        
        edges =[]
        
        for i in range(V):
            for j in adj[i]:
                edges.append([j[1],i,j[0]])
        
        edges.sort()
        
        uf = UnionFind(V)
        mstwt=0
        for x in edges:
            wt = x[0]
            u,v =x[1:]
            
            if uf.same(u,v):
                continue
            else:
                mstwt+=wt
                uf.merge(u,v)
        
        return mstwt
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends