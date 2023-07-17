pow5 = [5**x for x in range(15)]
pow5= set(pow5)

# print(pow5)
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        
        INF = 10**9
        
        n=len(s)
                
        def recur(idx):
            if idx>=n:
                return 0
            
            
            ans = INF
            if s[idx] =="0":
                return ans
            
            for j in range(idx,n):
                string = s[idx:j+1]
                if int(string,2) in pow5:
                    ans=min(ans,1+recur(j+1))
            
            return ans
        res = recur(0)
        
        return res if res!=INF else -1
            
            
            
        return recur(0,"")