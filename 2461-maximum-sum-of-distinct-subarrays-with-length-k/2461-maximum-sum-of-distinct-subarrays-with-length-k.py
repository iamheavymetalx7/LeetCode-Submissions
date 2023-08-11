class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        n=len(nums)
        l=0
        dic = defaultdict(int)
        summ=0
        maxi=0
        
        for r in range(n):
            
            while nums[r] in dic or r-l==k:
                if r-l==k:
                    maxi=max(maxi,summ)
                dic[nums[l]]-=1
                summ-=nums[l]
                if dic[nums[l]]==0:
                    del dic[nums[l]]
                        
                l+=1
            summ+=nums[r]
            dic[nums[r]]+=1
            
            
        if r+1-l==k:
            maxi= max(maxi,summ)
        return maxi