'''
1. https://leetcode.com/problems/largest-number/discuss/3954340/Python-or-Simple-Solution
2. https://leetcode.com/problems/largest-number/discuss/3950607/Python-3-Solution-or-O(n-log-n)

https://leetcode.com/problems/largest-number/discuss/3909031/Python-3


'''

class LargeNumber(str):
    def __lt__(x,y):
        return x+y>y+x
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        
        nums.sort(key = LargeNumber)
        
        string = ''.join(nums)
        
        return str(int(string))
        