class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        
        ans=0
        
        for j in range(30,-1,-1):
            is_set =False
            
            for el in nums:
                if (el & (1<<j)):
                    is_set=True
                    break
            
            if is_set:
                ans |= 1<<j
        return ans