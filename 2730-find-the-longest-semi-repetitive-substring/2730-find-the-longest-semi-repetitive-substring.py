class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        cur,i=0,0
        n=len(s)
        if n==1:
            return 1
        ans=0
        for j in range(1,n):
            cur+=(s[j]==s[j-1])
            
            while cur>1:
                i+=1
                cur-=(s[i]==s[i-1])
                ans=max(ans,j-i+1)
        ans=max(ans,j-i+1)
        return ans