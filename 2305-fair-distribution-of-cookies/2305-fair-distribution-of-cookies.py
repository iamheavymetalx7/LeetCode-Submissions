class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        bags=[0]*(k)
        
        n=len(cookies)
        
        ans = int(1e19)
        
        def dfs(idx):
            nonlocal ans
            if idx>=n:
                res = -int(1e19)
                for i in range(k):
                    res=max(res,bags[i])
                
                ans=min(ans,res)
                return
                
            for j in range(k):
                bags[j]+=cookies[idx]
                dfs(idx+1)
                bags[j]-=cookies[idx]
                if bags[j]==0:
                    break
            
            
            
        dfs(0)
        return ans