class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        l=0
        r=10**18
        
        n=len(nums)
        print(n)
        total_length=n+maxOperations
        
        summ=sum(nums)
        
        while r>l+1:
            
            m=(l+r)//2
            
            val = sum([math.ceil(x/m) for x in nums])
            

            if m*total_length>=summ and val<=total_length:
                r=m
            else:
                l=m
        
        return r
            

            
            
        