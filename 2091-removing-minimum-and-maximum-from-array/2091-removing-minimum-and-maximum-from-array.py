class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        maxi,mini = -int(1e19),int(1e19)
        n=len(nums)
        if n==1:
            return 1
        for x in nums:
            maxi=max(x,maxi)
            mini = min(x,mini)
        
        maxi_idx = nums.index(maxi)
        mini_idx = nums.index(mini)
        
        val1 = maxi_idx+1 +(n-mini_idx)
        val2 = mini_idx+1+(n-maxi_idx)
        val3 = maxi_idx+1+abs(mini_idx-maxi_idx)
        val4 = mini_idx+1+abs(maxi_idx-mini_idx)
        val5 = (n-mini_idx)+abs(mini_idx-maxi_idx)
        val6 = (n-maxi_idx)+abs(maxi_idx-mini_idx)
        # print(val1,val2,val3,val4,val5,val6)
        return min(val1,val2,val3,val4,val5,val6)