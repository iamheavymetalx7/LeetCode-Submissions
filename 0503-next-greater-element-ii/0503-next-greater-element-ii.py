class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nextg =[-1]*(n)
        
        st=[]
        
        for j in range(2):              ## just loop twice for the code of next greater element
            for i in range(n):
                while st and nums[st[-1]]<nums[i]:
                    idx = st.pop()
                    nextg[idx] = nums[i]
                st.append(i)
            
            
            
            
        return (nextg)