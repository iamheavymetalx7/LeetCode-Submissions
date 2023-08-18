class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        l=0
        ans=0
        n=len(s)
        
        for r in range(n):
            maxCost-=abs(ord(s[r])-ord(t[r]))
            
            while maxCost<0:
                maxCost+=abs(ord(s[l])-ord(t[l]))
                l+=1
            ans=max(ans,r-l+1)
        return ans