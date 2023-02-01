class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n=len(str1)
        m=len(str2)
        i,j=0,0
        
        ans=""
        to_ret=""
        
        
        while i<n and j<m:
            if str1[i]!=str2[j]:
                return ""
            ans+=str1[i]
            val1=n//len(ans)
            val2=m//len(ans)
            if ans*val1==str1 and ans*val2==str2:
                if len(to_ret)<len(ans):
                    to_ret = ans
            i+=1
            j+=1
                    
        return to_ret