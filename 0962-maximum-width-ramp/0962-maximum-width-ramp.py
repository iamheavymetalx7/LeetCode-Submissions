# class Solution: O(N* log (N)) code, see my code submitted on 17/06/23 -- @22:05
#     def maxWidthRamp(self, nums: List[int]) -> int:
#         arr=[]
        
#         for i,el in enumerate(nums):
#             arr.append([el,i])
        
#         n=len(nums)
        
#         mn=n
#         ans=0
        
        
#         arr.sort()

#         for i in range(n) :
#             ans= max(ans,arr[i][1]-mn)
#             mn = min(mn,arr[i][1])
        
#         return ans
                
            


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        st=[]
        n=len(nums)
        
        
        for i in range(n):
            if not st or nums[st[-1]]>nums[i]:
                st.append(i)
        
        # print(st)
        
        ans =0
        
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]<=nums[i]:
                idx = st.pop()
                ans=max(ans, abs(idx-i))
        
        return ans
                
            