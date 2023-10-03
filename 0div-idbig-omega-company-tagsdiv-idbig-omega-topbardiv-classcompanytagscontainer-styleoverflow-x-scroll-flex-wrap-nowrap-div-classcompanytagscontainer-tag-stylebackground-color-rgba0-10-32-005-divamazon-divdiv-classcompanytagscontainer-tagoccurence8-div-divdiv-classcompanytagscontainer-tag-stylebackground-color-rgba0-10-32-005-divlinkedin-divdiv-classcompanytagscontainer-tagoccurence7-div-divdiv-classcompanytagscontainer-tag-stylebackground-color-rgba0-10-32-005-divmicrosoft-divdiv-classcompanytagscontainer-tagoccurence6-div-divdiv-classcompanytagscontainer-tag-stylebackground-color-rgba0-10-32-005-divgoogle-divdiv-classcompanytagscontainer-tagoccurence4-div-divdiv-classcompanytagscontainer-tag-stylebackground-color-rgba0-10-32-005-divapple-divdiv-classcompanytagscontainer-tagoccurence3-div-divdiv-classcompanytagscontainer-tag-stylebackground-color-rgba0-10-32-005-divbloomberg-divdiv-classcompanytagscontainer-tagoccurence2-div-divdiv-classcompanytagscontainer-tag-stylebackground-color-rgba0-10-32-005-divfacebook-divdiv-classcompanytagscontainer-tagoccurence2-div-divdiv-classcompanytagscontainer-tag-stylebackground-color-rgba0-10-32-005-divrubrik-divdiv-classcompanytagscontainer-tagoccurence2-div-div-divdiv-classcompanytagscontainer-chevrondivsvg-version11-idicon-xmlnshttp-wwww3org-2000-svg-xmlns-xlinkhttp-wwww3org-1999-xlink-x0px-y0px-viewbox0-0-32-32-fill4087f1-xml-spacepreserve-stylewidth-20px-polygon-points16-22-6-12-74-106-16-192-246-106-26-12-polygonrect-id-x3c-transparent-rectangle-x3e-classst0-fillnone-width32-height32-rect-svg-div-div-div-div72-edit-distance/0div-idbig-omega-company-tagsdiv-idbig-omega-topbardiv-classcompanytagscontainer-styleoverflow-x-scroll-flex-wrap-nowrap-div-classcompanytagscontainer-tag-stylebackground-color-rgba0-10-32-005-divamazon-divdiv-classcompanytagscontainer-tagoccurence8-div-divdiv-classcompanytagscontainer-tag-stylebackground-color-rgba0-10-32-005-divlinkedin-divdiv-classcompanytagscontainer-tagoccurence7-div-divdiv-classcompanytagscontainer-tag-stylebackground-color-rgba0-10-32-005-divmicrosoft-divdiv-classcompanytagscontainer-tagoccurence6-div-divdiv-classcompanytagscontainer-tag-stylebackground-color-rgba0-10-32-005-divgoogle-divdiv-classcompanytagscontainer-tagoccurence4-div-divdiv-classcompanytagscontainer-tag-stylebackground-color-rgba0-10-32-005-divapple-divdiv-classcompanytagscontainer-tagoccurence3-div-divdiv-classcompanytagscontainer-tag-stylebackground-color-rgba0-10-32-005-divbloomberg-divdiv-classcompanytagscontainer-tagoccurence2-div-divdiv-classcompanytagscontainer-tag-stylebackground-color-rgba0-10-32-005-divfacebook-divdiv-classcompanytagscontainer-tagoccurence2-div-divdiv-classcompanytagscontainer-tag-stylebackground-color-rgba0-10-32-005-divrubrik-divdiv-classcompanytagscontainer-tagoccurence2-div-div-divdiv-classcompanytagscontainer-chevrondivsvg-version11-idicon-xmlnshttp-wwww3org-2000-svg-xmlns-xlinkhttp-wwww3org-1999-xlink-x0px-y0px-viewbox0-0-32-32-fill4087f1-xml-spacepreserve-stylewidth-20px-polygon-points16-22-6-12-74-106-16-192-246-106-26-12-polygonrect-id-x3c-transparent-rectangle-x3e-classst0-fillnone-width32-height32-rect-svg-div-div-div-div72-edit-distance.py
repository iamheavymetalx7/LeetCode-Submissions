class Solution:
    def minDistance(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        @cache
        def recur(i,j):
            if i>=m:
                return n-j
            if j>=n:
                return m-i
            ans = int(1e19)
            if s[i]==t[j]:
                ans = 0+recur(i+1,j+1)

            else:
                ans = 1+min(ans,recur(i+1,j+1),recur(i+1,j),recur(i,j+1))
                
            return ans
        val = recur(0,0)
        return val
        
