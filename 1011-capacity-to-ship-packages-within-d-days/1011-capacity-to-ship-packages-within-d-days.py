class Solution:
    def isPossible(self,m,weights,days):
        n=len(weights)
        cnt=1
        summ=0
        for i in range(len(weights)):
            summ+=weights[i]
            if weights[i]>m:
                return False
            if summ>m:
                # print(m,summ)
                cnt+=1
                summ=weights[i]
        return cnt<=days
    
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l=0;r=int(1e9)
        
        while r>l+1:
            m=(l+r)//2
            if self.isPossible(m,weights,days):
                r=m
            else:
                l=m
        return r
                