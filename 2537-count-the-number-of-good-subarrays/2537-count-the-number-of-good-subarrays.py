from collections import defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        n=len(nums)
        cnt=0
        dic=defaultdict(int)
        dic[nums[l]]+=1
        pairs=0
        pairs+=dic[nums[r]]-1
        
        while l<n:
            while pairs<k and r+1<n:
                r+=1
                
                dic[nums[r]]+=1
                pairs+=dic[nums[r]]-1
            if pairs>=k:
                cnt+=n-r
            if dic[nums[l]]>1:
                pairs-=dic[nums[l]]-1
            dic[nums[l]]-=1
            l+=1
        return cnt