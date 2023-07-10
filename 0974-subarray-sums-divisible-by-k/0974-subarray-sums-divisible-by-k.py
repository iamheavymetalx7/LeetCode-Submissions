class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        n=len(nums)
        dic[0]=1
        
        curr,ans=0,0
        
        for i in range(n):
            curr+=nums[i]
            if (curr)%k in dic:
                ans+=dic[curr%k]
            dic[curr%k]+=1
        return ans