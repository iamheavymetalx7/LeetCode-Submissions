class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n=len(nums)
        inf = int(1e19)
        mini = [inf for _ in range(n)]
        
        res = inf
        
        
        for k in range(n):
            s=k*x
            
            for i in range(n):
                mini[i]=min(mini[i],nums[(i+k)%n])
                s+=mini[i]
            
            res=min(res,s)
        return res
            