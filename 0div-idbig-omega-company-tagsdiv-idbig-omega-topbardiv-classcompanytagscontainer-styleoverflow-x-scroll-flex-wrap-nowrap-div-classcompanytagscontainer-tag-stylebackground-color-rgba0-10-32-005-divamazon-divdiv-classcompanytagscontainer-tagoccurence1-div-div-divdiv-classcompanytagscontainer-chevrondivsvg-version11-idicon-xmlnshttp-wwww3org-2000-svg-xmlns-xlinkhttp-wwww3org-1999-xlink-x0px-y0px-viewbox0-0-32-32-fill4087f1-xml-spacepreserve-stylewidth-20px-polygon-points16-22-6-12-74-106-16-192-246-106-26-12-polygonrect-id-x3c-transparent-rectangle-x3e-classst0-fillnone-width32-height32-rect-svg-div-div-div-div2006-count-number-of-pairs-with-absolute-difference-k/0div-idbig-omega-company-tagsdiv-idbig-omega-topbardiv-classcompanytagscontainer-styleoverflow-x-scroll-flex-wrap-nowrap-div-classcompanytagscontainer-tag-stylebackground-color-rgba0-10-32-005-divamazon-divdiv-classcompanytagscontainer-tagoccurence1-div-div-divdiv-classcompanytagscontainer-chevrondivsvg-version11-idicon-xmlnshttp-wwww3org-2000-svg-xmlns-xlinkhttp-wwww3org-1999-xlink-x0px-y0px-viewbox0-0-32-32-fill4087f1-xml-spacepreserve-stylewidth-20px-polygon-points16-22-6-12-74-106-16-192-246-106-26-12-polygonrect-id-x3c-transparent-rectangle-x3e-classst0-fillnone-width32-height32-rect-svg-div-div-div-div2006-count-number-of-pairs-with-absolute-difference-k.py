class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        dic = defaultdict(int)
        ans=0
        n=len(nums)
        for i in range(n):
            
            if (nums[i]+k) in dic:
                

                ans+=dic[nums[i]+k]
                
            if (nums[i]-k) in dic:
                ans+=dic[nums[i]-k]
                
            dic[nums[i]]+=1

        return ans