class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        newNums = list(set(nums))
        newNums.sort()
        ans =n
        
        for j in range(len(newNums)):
            right = newNums[j]+n-1
            idx = bisect_right(newNums,right)
            count = idx-j
            ans = min(ans,n-count)
        return ans