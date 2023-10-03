class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic= Counter(nums)
        ans =0
        
        for k,v in dic.items():
            ans+=((v)*(v-1))//2
            
        return ans