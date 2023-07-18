class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        k = len(strs)
        
        dp=[[[-1 for _ in range(101)]for _ in range(101)]for _ in range(k)]
        
        a=[]
        for ele in strs:
            one = ele.count("1")
            zero = ele.count("0")
            a.append([zero,one])
            
        def recur(idx,cnt0,cnt1):
            if idx==k and cnt0<=m and cnt1<=n:
                return 0
            
            if cnt0+a[idx][0]>m or cnt1+a[idx][1]>n:      ## missing base case (i missed)
                return recur(idx+1,cnt0,cnt1)
            
            if dp[idx][cnt0][cnt1]!=-1:
                return dp[idx][cnt0][cnt1]
            
            nottake = recur(idx+1,cnt0,cnt1)

            take =0
            take = 1+recur(idx+1,cnt0+a[idx][0],cnt1+a[idx][1])

            ans = max(take, nottake)

            dp[idx][cnt0][cnt1]=ans

            return dp[idx][cnt0][cnt1]
        ans = recur(0,0,0)
        
        return ans

        recur(0,0,0)
            
            
            
            
            
        