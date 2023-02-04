from collections import deque, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        q=deque()
        
        c1= Counter(s1)
        
        n,m=len(s1),len(s2)
        
        for i in range(min(n,m)):
            q.append(s2[i])
        
        c2=Counter(q)
        
        if c1==c2:
            return True
        
        for i in range(n,m):
            char=q.popleft()
            ele=s2[i]
            q.append(ele)
            
            c2[char]-=1
            c2[ele]+=1
            
            if c1==c2:
                return True
        return False
                