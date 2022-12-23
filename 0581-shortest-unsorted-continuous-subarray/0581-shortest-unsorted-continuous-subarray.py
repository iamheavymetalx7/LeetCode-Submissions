class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
    ## with space
        low=len(nums)-1
        high=0
        st=[]

        for i in range(len(nums)):
            while st and nums[st[-1]]>nums[i]:
                low=min(low,st.pop())
            st.append(i)
        st=[]
        for j in range(len(nums)-1,-1,-1):
            while st and nums[st[-1]]<nums[j]:
                high=max(high,st.pop())
            st.append(j)
        
        if low>=high: return 0
        
        return high-low+1