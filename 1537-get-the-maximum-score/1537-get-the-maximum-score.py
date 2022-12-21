class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        mod=10**9+7
        i=0
        j=0
        s=0
        s1,s2=0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                s1+=nums1[i]
                i+=1
            elif nums2[j]<nums1[i]:
                s2+=nums2[j]
                j+=1

            elif nums1[i]==nums2[j]:
                s += max(s1,s2)+nums2[j]
                s1=0
                s2=0
                i+=1
                j+=1
        
        while i<len(nums1):
            s1+=nums1[i]
            i+=1
            
        while j<len(nums2):
            s2+=nums2[j]
            j+=1
        
        s+=max(s1,s2)
        
        s =s % mod
        
        return s
        
        
            