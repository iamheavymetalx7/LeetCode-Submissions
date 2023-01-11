from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        
        res=round(log(n,3))
        
        # print(res)
        
        return 3**res==n
