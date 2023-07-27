class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        low,high =0,int(1e8)
        
        n=len(dist)
        
        
        def isPossible(x):
            hr =0
            
            for i in range(n-1):
                hr+=(dist[i]+(x-1))//x
            
            hr+=(dist[-1])/x
            
            # print(hr)
            
            if hr>hour:
                return False
            return True
        
        while high-low>1:
            mid = (high+low)//2
            
            # print(mid)
            
            if isPossible(mid):
                high = mid
            else:
                low = mid
        if high==int(1e8):
            return -1
        return (high)