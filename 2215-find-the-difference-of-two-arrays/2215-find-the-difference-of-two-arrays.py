class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        cf1=Counter(nums1)
        cf2=Counter(nums2)
        
        ans=[[],[]]
        
        for k in cf1.keys():
            if k not in cf2:
                ans[0].append(k)
        
        for k in cf2.keys():
            if k not in cf1:
                ans[1].append(k)
        
        return ans