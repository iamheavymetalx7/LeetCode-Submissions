class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        summ = sum(nums)
        n=len(nums)

        
        g =[[] for _ in range(n)]
        degree =[ 0 for _ in range(n)]
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
            degree[x]+=1
            degree[y]+=1
        
        
        divisors =[]
        # print(int(math.sqrt(summ))+1)
        for i in range(1,int(math.sqrt(summ))+1):
            if summ%i==0:
                if i!=summ//i:
                    divisors.append(i)
                    divisors.append(summ//i)
                else:
                    divisors.append(i)
        divisors.sort()
        # print(divisors)
        
        def bfs(target):
            deg = degree[:]
            vals =nums[:]
            
            q=deque()
            for i,dd in enumerate(degree):
                if dd==1:
                    q.append(i)
            
            while q:
                ci = q.popleft()
                deg[ci]=0
                # print(ci,g[ci])
                for to in g[ci]:
                    
                    if vals[ci]!=target:
                        vals[to]+=vals[ci]
                        
                    deg[to]-=1
                    if deg[to]==0:
                        return vals[to]==target
                    elif deg[to]==1:
                        q.append(to)
                        
                    
        
        
        for d in divisors:
            if bfs(d):
                return summ//(d) - 1
            
        return 0



                        
                        
                    
                
            
            
            
        
            
            
    
        