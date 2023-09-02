class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        
        def createNei(x):
            for i in range(4):
                curr = int(x[i])
                for diff in (-1,1):
                    new = (curr+diff+10)%10
                    yield x[:i]+str(new)+x[i+1:]
                    
        if "0000" in deadends_set:
            return -1
        cur ="0000"
        q=deque()
        q.append(cur)
        
        
        steps =0
        
        while q:
            n = len(q)
            for _ in range(n):
                now = q.popleft()
                if now==target:
                    return steps
                
                for nei in createNei(now):
                    if nei in deadends_set:
                        continue
                    deadends_set.add(nei)
                    q.append(nei)
            steps+=1
        return -1
                    
                    
            