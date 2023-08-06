class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ## sum(max()-min())
        ##sum(max()) - sum(min())
        ## take help of sum of subarray minimums
        
        
        st=[]
        minsum = 0
        n=len(nums)
        
        
        for next_smaller in range(n+1):
            
            while st and (next_smaller==n or nums[st[-1]]>nums[next_smaller]):
                i=st.pop()
                prev = st[-1] if st else -1
                minsum+=nums[i]*(i-prev)*(next_smaller -i)
            st.append(next_smaller)
        # print(minsum)
        
        st=[]
        n=len(nums)
        
        maxsum =0
        for next_big in range(n+1):
            print(next_big,st)
            while st and (next_big==n or nums[st[-1]]<nums[next_big]):
                i=st.pop()
                prev = st[-1] if st else -1
                maxsum += nums[i]*(i-prev)*(next_big-i)
            st.append(next_big)
        # print(maxsum)
        
        return maxsum-minsum