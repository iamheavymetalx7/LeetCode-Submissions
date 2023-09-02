class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ## since limit -> we take max and min and then move ahead
        
        n = len(nums)
        dic = defaultdict(int)
        l=0
        ans= 0
        for r in range(n):
            dic[nums[r]]+=1
            # print(r,dic,"here")
            while dic and (max(dic)-min(dic))>limit:
                dic[nums[l]]-=1
                if dic[nums[l]]==0:
                    del dic[nums[l]]
                
                l+=1
                
            ans=max(ans,r-l+1)
        ans = max(ans,r-l+1)
                
        return ans