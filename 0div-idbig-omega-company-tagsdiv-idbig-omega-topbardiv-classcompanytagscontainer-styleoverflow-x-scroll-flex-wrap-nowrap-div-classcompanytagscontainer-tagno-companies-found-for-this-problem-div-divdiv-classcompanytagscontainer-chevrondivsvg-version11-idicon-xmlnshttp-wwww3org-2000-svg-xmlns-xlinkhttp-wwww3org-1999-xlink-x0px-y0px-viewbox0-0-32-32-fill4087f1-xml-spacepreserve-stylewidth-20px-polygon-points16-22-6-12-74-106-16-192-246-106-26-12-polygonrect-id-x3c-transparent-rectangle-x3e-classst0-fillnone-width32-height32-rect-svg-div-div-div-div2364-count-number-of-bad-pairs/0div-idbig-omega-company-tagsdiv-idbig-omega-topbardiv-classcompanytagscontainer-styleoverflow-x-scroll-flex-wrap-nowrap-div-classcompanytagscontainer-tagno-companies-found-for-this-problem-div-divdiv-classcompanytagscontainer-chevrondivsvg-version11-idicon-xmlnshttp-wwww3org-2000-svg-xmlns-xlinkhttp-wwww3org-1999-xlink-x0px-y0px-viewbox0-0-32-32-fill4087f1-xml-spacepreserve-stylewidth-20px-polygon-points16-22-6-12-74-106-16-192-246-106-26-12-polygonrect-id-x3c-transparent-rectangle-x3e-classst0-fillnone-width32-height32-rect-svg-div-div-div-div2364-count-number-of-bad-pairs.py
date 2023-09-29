class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            nums[i] = i-nums[i]
        
        # print(*nums)
        
        
        ans =0
        dic = defaultdict(int)
        
        for i in range(n):
            if nums[i] in dic:
                ans+=dic[nums[i]]
            
            dic[nums[i]]+=1
        
        return (n*(n-1))//2-ans
        
            