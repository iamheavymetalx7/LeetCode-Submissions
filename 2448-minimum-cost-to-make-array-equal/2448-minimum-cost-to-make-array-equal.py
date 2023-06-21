class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        arr = list(zip(nums,cost))
        
        arr.sort()
        cnt=0
        
        summ = sum(cost)
        
        for n,c in arr:
            cnt+=c
            
            if cnt>summ//2:
                val = n
                break
        
        print(val)
            
        return sum(abs(x-val)*(c) for x,c in arr)
            
            
        