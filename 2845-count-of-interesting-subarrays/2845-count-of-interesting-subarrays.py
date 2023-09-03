class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n=len(nums)
        
        for i in range(n):
            if nums[i]%modulo==k:
                nums[i]=1
            else:
                nums[i]=0
        
        
            
        dic=defaultdict(int)
        dic[0]=1
        ans =0
        x=0
        for i in range(n):
            x+=(nums[i])
            x%=modulo
            
            to_find = (x-k)%modulo
            
            if to_find in dic:
                ans+=dic[to_find]
            dic[x]+=1
        return ans
            