from collections import Counter, deque
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        ans=[]
        
        if len(p)>len(s):
            return []
        
        c1=Counter(p)
        q=deque()
        for i in range(m):
            q.append(s[i])
        
        c2=Counter(q)
        
        if c1==c2:
            ans.append(0)
            
        for i in range(m,n):
            ele=q.popleft()
            c2[ele]-=1
            c2[s[i]]+=1
            q.append(s[i])
            
            if c1==c2:
                ans.append(i+1-m)
        
            
        return ans
        