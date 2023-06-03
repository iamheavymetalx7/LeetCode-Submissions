class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        dic = defaultdict(list)
        n=len(bombs)
        
        for i in range(n):
            x,y,r = bombs[i]
            for j in range(n):
                if j==i:
                    continue
                
                x2,y2,r2=bombs[j]
                if (x2-x)**2+(y2-y)**2<=r**2:
                    dic[i].append(j)
        
        ans=1
        for i in range(n):
            vis=set()
            ele = i
            q=deque()
            q.append(ele)
            vis.add(ele)
            mx=0    

            while q:
                node = q.popleft()
                mx+=1
                

                for nei in dic[node]:
                    if nei not in vis:
                        vis.add(nei)
                        q.append(nei)
            
        
            ans=max(ans,mx)
        return ans