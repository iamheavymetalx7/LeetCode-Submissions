class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums= []
        nums.append(nums1)
        nums.append(nums2)
        n = len(nums1)
        @cache
        def recur(prv_num,ind):
            if ind>=n:
                return 0
            ans =0
            for j in range(2):
                if nums[prv_num][ind-1] <= nums[j][ind]:
                    ans =max(ans,1+recur(j,ind+1))
            return ans
        
        val =1
        for j in range(n-1):
            val = max(val,1+recur(0,j+1))
            val = max(val,1+recur(1,j+1))
        return val