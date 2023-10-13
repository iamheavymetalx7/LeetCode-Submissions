class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        m = len(target)
        mx = (1<<m)-1
        n= len(stickers)
        
        dp = [-1 for _ in range(mx+10)]
            
        def recur(mask):
            if mask == (mx):
                return 0
            
            if dp[mask]!=-1:
                return dp[mask]
            
            ans = int(1e19)
            
            for i in range(n):
                cnt = [0]*(26)
                for j in range(len(stickers[i])):
                    cnt[ord(stickers[i][j])-ord('a')]+=1
                # print(i,cnt)
                newmask =0
                
                for j in range(m):
                    if ((1<<j)&(mask))==0:
                        if cnt[ord(target[j])-ord('a')]>0:
                            cnt[ord(target[j])-ord('a')]-=1
                            newmask |= (1<<j)
                if newmask!=0:
                    ans = min(ans,1+recur(mask|newmask))
            dp[mask] = ans
            return dp[mask]
        
        val = recur(0)
        if val == int(1e19):
            return -1
        return val
                        
            
            
            