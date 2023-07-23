class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n=len(nums)
        minimums = [0]*(n)
        
        st=[]
        
        for i in range(n):
            if i==0:
                minimums[i]=0
            else:
                if nums[i]<nums[minimums[i-1]]:
                    minimums[i]=i
                else:
                    minimums[i]=minimums[i-1]
        
        
            while st and nums[st[-1]]<=nums[i]:
                st.pop()
            if st:

                if nums[minimums[st[-1]]]<nums[i]:
                    return True
            st.append(i)

        return False
        
            