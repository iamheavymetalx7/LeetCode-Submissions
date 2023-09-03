class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        #j-i!=nums[j]-nums[i]
        #==> i-nums[i]!=(j-nums[j])
        n=len(nums)
        
        for i in range(n):
            nums[i]=i-nums[i]
        
        # print(nums)
        
        dic=defaultdict(int)
        
        ans = 0
        
        for i in range(n):
            if nums[i] in dic:
                ans+= dic[nums[i]]
            
            dic[nums[i]]+=1
        
        return (n*(n-1))//2-(ans)