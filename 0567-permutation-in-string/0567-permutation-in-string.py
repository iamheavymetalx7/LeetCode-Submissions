from collections import deque,Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        c1=Counter(s1)
        
        q=deque()
        
        for i in range(min(k,len(s2))):
            q.append(s2[i])
            
        
        c2=Counter(q)
        
        if c1==c2:
            return True
        
        for i in range(k,len(s2)):
            char = q.popleft()
            q.append(s2[i])
            c2[char]-=1
            c2[s2[i]]+=1
            if c1==c2:
                return True
        
        return False
            
            
        
        
        
        