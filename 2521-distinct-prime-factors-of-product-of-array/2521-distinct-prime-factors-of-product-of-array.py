
mx = 1000
spf = [i for i in range(mx+1)]
i=2
while i*i<=mx:
    if spf[i]==i:
        for j in range(i*i,mx+1,i):
            spf[j]=min(spf[j],i)
    i+=1
            
def getPrimeFactors(x):
    while x!=1:
        yield spf[x]
        x//=spf[x]


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        
        seen=set()       
        
        for ele in nums:
            for fac in getPrimeFactors(ele):
                seen.add(fac)
        
        return len(seen)
            
