class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        indegree=[0]*(n)
        cf = defaultdict(list)
        
        edges = set()
        for x,y in roads:
            edges.add((x,y))
            edges.add((y,x))
        

        for x,y in roads:
            indegree[x]+=1
            indegree[y]+=1
            cf[x].append(y)
            cf[y].append(x)
        
        
        
        a = [(len(v),k) for k,v in cf.items()]
        

        a.sort(reverse=True)

        ans=0
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                tot=a[i][0]+a[j][0]
                
                if (a[i][1],a[j][1]) in edges:
                    tot-=1
                ans=max(ans,tot)
        return ans
                    
                