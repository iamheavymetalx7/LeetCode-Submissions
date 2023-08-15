class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        dic=Counter(nums)
        ans =0
        for i in range(0,2*10**5+5):
            if dic[i]>1:
                ans+=dic[i]-1
                dic[i+1]+=dic[i]-1
        return ans