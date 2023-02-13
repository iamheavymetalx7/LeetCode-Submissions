import math
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans =  math.ceil((high-low)/2)
        
        if low%2 and high%2:
            ans+=1
        
        return ans