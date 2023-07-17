class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        dic=defaultdict(int)
        ans=0
        
        for r in range(n):
            dic[nums[r]]+=1
            
            while max(dic.keys())-min(dic.keys())>2:
                dic[nums[l]]-=1
                
                if dic[nums[l]]==0:
                    del dic[nums[l]]
                
                l+=1
            
            ans+=r-l+1
        return ans
        