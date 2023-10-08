class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1=len(nums1)
        n2=len(nums2)
        
        if max(nums1)<0 and min(nums2)>0:
            return max(nums1)*min(nums2)
        
        if min(nums1)>0 and max(nums2)<0:
            return min(nums1)*max(nums2)
        
        @cache
        def recur(i,j):
            if i>=n1 or j>=n2:
                return 0
            ans = -int(1e19)
            ans= max(ans,nums1[i]*nums2[j]+recur(i+1,j+1))
            ans = max(ans,max(recur(i+1,j),recur(i,j+1)))
            return ans
        
        val = recur(0,0)
        return val