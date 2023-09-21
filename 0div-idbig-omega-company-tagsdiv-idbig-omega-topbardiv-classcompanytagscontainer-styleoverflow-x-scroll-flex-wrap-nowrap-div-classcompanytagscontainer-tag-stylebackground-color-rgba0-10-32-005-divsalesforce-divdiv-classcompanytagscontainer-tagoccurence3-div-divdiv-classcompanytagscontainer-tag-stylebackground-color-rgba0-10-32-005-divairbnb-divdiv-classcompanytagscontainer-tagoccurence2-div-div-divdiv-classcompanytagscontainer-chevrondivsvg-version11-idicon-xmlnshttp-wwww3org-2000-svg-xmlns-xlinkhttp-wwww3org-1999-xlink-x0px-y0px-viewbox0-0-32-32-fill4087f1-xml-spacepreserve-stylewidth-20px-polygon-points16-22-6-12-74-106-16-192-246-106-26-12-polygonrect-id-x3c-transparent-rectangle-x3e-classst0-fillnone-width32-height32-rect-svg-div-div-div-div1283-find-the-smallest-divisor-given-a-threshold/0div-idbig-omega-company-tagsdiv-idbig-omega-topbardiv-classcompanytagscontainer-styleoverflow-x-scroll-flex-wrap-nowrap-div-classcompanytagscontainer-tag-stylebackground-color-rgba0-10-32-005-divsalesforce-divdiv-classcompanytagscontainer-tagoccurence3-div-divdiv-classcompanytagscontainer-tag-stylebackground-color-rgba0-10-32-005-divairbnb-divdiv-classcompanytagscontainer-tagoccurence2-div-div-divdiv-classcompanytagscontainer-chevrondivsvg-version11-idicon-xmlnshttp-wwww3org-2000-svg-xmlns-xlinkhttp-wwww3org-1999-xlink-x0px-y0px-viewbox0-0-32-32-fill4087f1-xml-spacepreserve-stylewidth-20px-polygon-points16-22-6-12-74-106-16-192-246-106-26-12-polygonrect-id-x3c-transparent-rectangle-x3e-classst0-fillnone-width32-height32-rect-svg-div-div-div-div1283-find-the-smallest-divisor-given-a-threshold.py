class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        l=0
        r=int(1e18)
        n=len(nums)
        
        def check(mid):
            ans= 0
            for i in range(n):
                ans+= (nums[i]+(mid-1))//mid
            return ans<=threshold
        
        while r-l>1:
            mid = (l+r)//2
            if check(mid):
                r=mid
            else:
                l=mid
        return r