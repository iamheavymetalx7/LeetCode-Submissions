class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dp=[1]*n
        nums.sort()
        
        maxi=1
        lastIndex=0
        
        has=[i for i in range(n)]
        
        for index in range(1,n):
            for j in range(index):
                if nums[index]%nums[j]==0 and dp[index]<dp[j]+1:
                    dp[index]=1+dp[j]
                    has[index]=j
        
            if dp[index] >maxi:
                maxi=dp[index]
                lastIndex =index
        arr=[]
        arr.append(nums[lastIndex])
        
        while has[lastIndex]!=lastIndex:
            lastIndex=has[lastIndex]
            arr.append(nums[lastIndex])
            
        return arr