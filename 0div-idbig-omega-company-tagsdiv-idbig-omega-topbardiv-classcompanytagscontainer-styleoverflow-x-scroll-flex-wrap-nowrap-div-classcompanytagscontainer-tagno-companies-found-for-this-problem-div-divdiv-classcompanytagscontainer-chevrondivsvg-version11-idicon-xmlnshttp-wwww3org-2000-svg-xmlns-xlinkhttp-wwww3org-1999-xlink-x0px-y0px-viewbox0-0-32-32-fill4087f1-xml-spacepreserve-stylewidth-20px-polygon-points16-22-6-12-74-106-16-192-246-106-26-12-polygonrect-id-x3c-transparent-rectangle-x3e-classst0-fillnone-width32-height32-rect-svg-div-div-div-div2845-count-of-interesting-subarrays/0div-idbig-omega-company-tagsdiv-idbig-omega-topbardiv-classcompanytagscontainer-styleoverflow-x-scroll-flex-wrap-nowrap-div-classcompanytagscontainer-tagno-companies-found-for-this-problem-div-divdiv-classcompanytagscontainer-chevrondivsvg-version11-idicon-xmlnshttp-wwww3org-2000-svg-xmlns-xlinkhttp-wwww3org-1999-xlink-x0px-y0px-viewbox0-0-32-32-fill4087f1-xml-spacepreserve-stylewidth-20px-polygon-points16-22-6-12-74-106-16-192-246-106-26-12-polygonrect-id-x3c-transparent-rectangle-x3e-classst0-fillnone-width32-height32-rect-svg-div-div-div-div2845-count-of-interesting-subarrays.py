class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n=len(nums)
        
        for i in range(n):
            if nums[i]%modulo==k:
                nums[i]=1
            else:
                nums[i]=0
        
        dic = defaultdict(int)
        dic[0]=1
        
        pref =0
        ans = 0
        
        for i in range(n):
            pref+=nums[i]
            pref%=modulo
            
            if ((pref-k)%modulo) in dic:
                ans+=dic[(pref-k)%modulo]
            
            dic[pref]+=1
        return ans
                
            
            
            