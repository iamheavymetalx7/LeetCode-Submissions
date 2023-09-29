class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0]=1
        
        n =len(nums)
        sum=0
        ans = 0
        for i in range(n):
            sum+=nums[i]
            sum%=k
            if (sum-k)%k in dic:
                ans+=dic[(sum-k)%k]
            dic[sum]+=1
        
        return ans
            
                
            