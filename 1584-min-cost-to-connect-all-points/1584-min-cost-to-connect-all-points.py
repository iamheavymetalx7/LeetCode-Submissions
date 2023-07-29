

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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                edges.append((i,j,dist))
        
        
        edges.sort(key = lambda x:x[2])
        
        mstwt =0
        
        uf = UnionFind(n)
        
        for x in edges:
            u,v = x[:2]
            wt = x[2]
            
            if uf.same(u,v):
                continue
            else:
                mstwt+=wt
                uf.merge(u,v)
        return mstwt
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        