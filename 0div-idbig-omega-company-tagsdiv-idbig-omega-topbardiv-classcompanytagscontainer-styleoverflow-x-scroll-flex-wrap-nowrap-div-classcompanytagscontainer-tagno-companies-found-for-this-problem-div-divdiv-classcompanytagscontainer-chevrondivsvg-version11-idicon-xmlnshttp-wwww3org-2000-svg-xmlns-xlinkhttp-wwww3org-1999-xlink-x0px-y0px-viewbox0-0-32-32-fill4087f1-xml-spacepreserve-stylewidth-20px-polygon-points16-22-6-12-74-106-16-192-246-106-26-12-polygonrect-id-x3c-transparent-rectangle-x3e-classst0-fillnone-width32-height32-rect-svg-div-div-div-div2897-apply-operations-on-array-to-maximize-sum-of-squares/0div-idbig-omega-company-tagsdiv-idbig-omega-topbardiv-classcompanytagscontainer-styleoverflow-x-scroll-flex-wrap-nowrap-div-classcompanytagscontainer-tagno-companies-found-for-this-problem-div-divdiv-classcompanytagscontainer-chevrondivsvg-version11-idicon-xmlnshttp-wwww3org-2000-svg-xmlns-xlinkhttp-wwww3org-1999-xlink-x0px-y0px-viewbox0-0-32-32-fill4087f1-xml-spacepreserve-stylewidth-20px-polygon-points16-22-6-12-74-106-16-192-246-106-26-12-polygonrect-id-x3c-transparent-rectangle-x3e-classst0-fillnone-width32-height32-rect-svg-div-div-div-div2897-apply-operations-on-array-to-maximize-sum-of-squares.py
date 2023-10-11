class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        cnt =[0]*(31)
        MOD = int(1e9)+7
        
        for i,n in enumerate(nums):
            for j in range(31):
                if (1<<j)&(n):
                    cnt[j]+=1
        
        ans =0
        for i in range(k):
            val =0
            for j in range(31):
                if cnt[j]<(i+1): continue
                val |= (1<<j)
            
            ans =(ans+val**2)%MOD
        return ans