class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i=0
        j=0
        
        if not s:
            return True
        if not t:
            return False
        
        
        
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
            if i==len(s):
                return True
            if j==len(t):
                return False
        