class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        mod=int(1e9)+7
        
        i,j=0,0
        s1,s2=0,0
        summ =0
        n,m=len(nums1),len(nums2)
        
        while i<n and j<m:
            if nums1[i]<nums2[j]:
                s1+=nums1[i]
                i+=1
            
            elif nums2[j]<nums1[i]:
                s2+=nums2[j]
                j+=1
            
            elif nums2[j]==nums1[i]:
                summ+=max(s1,s2)+nums1[i]
                i+=1
                j+=1
                s1,s2=0,0
        
        while i<n:
            s1+=nums1[i]
            i+=1
        
        while j<m:
            s2+=nums2[j]
            j+=1
        
        summ+=max(s1,s2)
        
        summ%=mod
        
        return summ
        