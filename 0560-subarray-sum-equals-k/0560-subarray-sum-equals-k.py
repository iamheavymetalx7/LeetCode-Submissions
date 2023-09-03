class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dic = defaultdict(int)
        dic[0]=1
        sum=0
        ans=0
        for i in range(n):
            sum+=nums[i]
     
            if (sum-k) in dic:
                ans+=dic[sum-k]
            dic[sum]+=1
        return ans
            