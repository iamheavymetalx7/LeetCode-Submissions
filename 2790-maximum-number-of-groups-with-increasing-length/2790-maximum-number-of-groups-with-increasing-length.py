class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        
        usageLimits.sort()
        
        total,cnt=0,0
        n=len(usageLimits)
        for i in range(n):
            total+=usageLimits[i]
            
            if total>=((cnt+1)*(cnt+2))//2:
                cnt+=1

        return cnt