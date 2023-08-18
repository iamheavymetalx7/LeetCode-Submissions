class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        l=0
        n=len(nums)
        ans=1
        
        dic=defaultdict(int)
        
        for r in range(n):
            
            dic[nums[r]]+=1
            
            while max(dic)-min(dic)>limit:
                dic[nums[l]]-=1
                
                if dic[nums[l]]==0:
                    del dic[nums[l]]
                
                l+=1
            ans=max(ans,r-l+1)
        return ans