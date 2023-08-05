class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        i=0
        j=0
        
        reqd = len(t)
        
        while i<len(s) and j<len(t):
            # print(i,j)
            if s[i]==t[j]:
                i+=1
                j+=1
                reqd-=1

            else:
                i+=1
        
        return reqd
            