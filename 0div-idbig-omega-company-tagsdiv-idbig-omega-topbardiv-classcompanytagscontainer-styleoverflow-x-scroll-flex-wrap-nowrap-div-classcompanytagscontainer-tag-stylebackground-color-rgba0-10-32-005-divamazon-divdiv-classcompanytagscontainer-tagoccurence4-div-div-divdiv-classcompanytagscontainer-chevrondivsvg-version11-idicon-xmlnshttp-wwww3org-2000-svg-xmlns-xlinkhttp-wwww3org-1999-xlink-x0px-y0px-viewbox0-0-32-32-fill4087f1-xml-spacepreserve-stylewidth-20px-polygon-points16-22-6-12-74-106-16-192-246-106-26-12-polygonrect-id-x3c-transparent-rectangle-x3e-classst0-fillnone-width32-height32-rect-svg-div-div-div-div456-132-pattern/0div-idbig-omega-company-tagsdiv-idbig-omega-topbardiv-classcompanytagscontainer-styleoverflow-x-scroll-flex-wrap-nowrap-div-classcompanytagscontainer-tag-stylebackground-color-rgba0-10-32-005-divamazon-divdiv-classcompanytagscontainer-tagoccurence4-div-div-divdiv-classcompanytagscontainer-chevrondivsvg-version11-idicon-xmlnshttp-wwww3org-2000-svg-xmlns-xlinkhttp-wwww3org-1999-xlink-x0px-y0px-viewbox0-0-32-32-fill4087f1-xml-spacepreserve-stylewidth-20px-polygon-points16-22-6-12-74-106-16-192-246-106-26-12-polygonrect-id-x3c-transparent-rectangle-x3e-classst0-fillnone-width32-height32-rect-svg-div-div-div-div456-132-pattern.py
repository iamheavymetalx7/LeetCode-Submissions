'''

https://leetcode.com/problems/132-pattern/discuss/94071/Single-pass-C%2B%2B-O(n)-space-and-time-solution-(8-lines)-with-detailed-explanation.
'''

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        
        s3 = -int(1e19)
        n=len(nums)
        st=[]
        
        for i in range(n-1,-1,-1):
            if nums[i]<s3:
                return True
            
            else:
                while st and nums[i]>st[-1]:
                    s3=st.pop()
                st.append(nums[i])
        return False