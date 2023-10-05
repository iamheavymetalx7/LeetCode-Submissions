class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        pref= [0]*(n+1)
        
        for i in range(1,n+1):
            pref[i] = pref[i-1]^nums[i-1]
        
        ans = [0 for _ in range(n)]   
        
        for i in range(n-1,-1,-1):
            val = pref[i+1]^pref[0]
            reqd = 0
            for j in range(maximumBit):
                if not val&(1<<j):
                    reqd|=(1<<j)
            ans[i]=reqd
        return ans[::-1]
                    
