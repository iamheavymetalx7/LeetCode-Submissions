class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], F: int, S: int) -> int:
        n=len(nums)
        prefix =[0]*(n+1)
        
        prefix[0]=0
        
        for i in range(1,n+1):
            prefix[i]=prefix[i-1]+nums[i-1]
        # print(prefix)
        maxm,maxl=0,0
        
        summ=0
        
        for x in range(F,len(prefix)-S):
            maxm = max(maxm,prefix[x]-prefix[x-F])
            summ = max(summ,maxm+prefix[x+S]-prefix[x])
            
        for x in range(S,len(prefix)-F):
            maxl = max(maxl,prefix[x]-prefix[x-S])
            summ = max(summ,maxl+prefix[x+F]-prefix[x])
        return summ