class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans=0
        is_neg=False
        
        for i in range(32):
            counter = 0
            
            for x in nums:
                if (x>>i)&1:
                    counter+=1
            
            if counter%3!=0:
                if i==31:
                    is_neg=True
                ans+=pow(2,i)
            
        return ans if not is_neg else ans-pow(2,32)