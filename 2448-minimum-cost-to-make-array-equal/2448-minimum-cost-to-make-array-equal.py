class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        arr = list(zip(nums,cost))

        arr.sort()
        
        total,cnt = sum(cost),0
        
        for n,c in arr:
            cnt+=c
            
            if cnt>total//2:
                target = n
                break
        
        tot=0
        for n,c in arr:
            tot+=abs(n-target)*c
        
        return tot