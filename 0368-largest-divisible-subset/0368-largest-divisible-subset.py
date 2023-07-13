class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        hashmap=[i for i in range(n)]
        dp=[1]*(n)
        maxi =1
        lastIndex =0
        
        for idx in range(1,n):
            for prev in range(idx):
                if nums[idx]%nums[prev]==0 and dp[idx]<1+dp[prev]:
                    dp[idx]=1+dp[prev]
                    hashmap[idx]=prev
            if dp[idx]>maxi:
                maxi = dp[idx]
                lastIndex = idx
        
        temp=[]
        temp.append(nums[lastIndex])
        
        while lastIndex != hashmap[lastIndex]:
            lastIndex = hashmap[lastIndex]
            temp.append(nums[lastIndex])
        
        
        return temp
        
                
                
                    
                    
        