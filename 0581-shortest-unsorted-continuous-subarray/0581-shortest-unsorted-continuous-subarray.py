class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        #two pointer
        n=len(nums)
        low=0
        high=len(nums)-1
        
        # find the first number out of sorting order from the beginning
        while low<len(nums)-1 and nums[low]<=nums[low+1]:
            low+=1
        
        if low==n-1:
            return 0
        
        # find the first number out of sorting order from the end
        while high>0 and nums[high]>=nums[high-1]:
            high-=1
        
        
        # find the maximum and minimum of the subarray

        maxi=max(nums[low:high+1])

        mini=min(nums[low:high+1])
        
        # extend the subarray to include any number which is bigger than the minimum of 
        # the subarray
        while low>0 and nums[low-1]>mini:
            low-=1
            
            
        # extend the subarray to include any number which is smaller than the maximum of 
        # the subarray    
        while high<len(nums)-1 and nums[high+1]<maxi:
            high+=1
            
        return high-low+1


        
        
        
        
        
        
        
        
        
#     ## with space
#         low=len(nums)-1
#         high=0
#         st=[]

#         for i in range(len(nums)):
#             while st and nums[st[-1]]>nums[i]:
#                 low=min(low,st.pop())
#             st.append(i)
#         st=[]
#         for j in range(len(nums)-1,-1,-1):
#             while st and nums[st[-1]]<nums[j]:
#                 high=max(high,st.pop())
#             st.append(j)
        
#         if low>=high: return 0
        
#         return high-low+1