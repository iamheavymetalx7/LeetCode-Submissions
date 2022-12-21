class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        arr=[0]*(max(nums)+1)
        
        for num in nums:
            arr[num]+=num
        
        size=len(arr)
        dp=[-1]*size
        
        if size<=2:
            return max(arr)
        
        def recur(nums,index):
            if index>=len(nums):
                return 0
            if dp[index]!=-1:
                return dp[index]
            
            take=recur(nums,index+2)+nums[index]
            nottake=recur(nums,index+1)
            
            dp[index] = max(take,nottake)
            
            return dp[index]
        
        return recur(arr,0)
        