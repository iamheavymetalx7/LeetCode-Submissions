class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n=len(nums)
        
        if n==1:
            if k%2!=0:
                return -1
            return nums[0]
        
        if k==0:
            return nums[0]
        
        if k==1:
            return nums[1]
        if k==n:
            return max(nums[:n-1])
        if k>n:
            return max(nums)
        
        m=max(nums[:k-1])
        m=max(m,nums[k])
        
        return m