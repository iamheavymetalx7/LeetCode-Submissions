class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n=len(s)
        tot = 0
        for i in range(len(s)):
            
            if s[i].isdigit():
                tot*=int(s[i])
                
            else:
                tot+=1
        
        for c in reversed(s):
            k%=tot
            if k==0 and c.isalpha():
                return c
            elif c.isdigit():
                tot//=int(c)
            else:
                tot-=1
                
        
                
            