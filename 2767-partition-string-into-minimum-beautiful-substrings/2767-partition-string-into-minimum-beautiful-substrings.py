pow5 = [5**x for x in range(15)]
pow5= set(pow5)


## similar to palindrome partitioning!!

                    
# print(pow5)
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        
        INF = 10**9
        
        n=len(s)
        
        dp=[-1]*(n)
                
        def recur(idx):
            if idx>=n:
                return 0
            
            if dp[idx]!=-1:
                return dp[idx]
            
            
            
            ans = INF
            if s[idx] =="0":
                return ans
            
            for j in range(idx,n):
                string = s[idx:j+1]
                if int(string,2) in pow5:
                    ans=min(ans,1+recur(j+1))
            dp[idx]=ans
            return dp[idx]
        res = recur(0)
        
        return res if res!=INF else -1
            
            
            
        return recur(0,"")