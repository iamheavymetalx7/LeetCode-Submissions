class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        dic = defaultdict(int)
        dic[0]=1
        
        psum=0;res=0
        
        for x in nums:
            psum+=x
            res+=dic[psum-goal]
            dic[psum]+=1
        return res
            