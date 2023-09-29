'''
nums[i]+ rev(nums[j]) = nums[j] + rev(nums[i])

=> nums[i] - rev(num[i]) = nums[j] - rev(num[j])

'''

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        n = len(nums)
        dic = defaultdict(int)
        ans =0
        MOD = int(1e9)+7
        
        for i in range(n):
            x = nums[i]
            y = str(x)
            y = y[::-1]
            y = int(y)
            
            if (x-y) in dic:
                ans+=dic[(x-y)]
                ans%=MOD
                
            
            dic[x-y]+=1
        return ans%MOD
    
        