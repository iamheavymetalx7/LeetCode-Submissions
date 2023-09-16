'''
1.https://leetcode.com/problems/can-i-win/discuss/404665/Java-DP-solution-with-detailed-explanation-very-easy-to-understand

2. https://leetcode.com/problems/can-i-win/discuss/850051/Python3-top-down-dp

'''

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal<=0:
            return True
        
        if (maxChoosableInteger*(maxChoosableInteger+1))//2<desiredTotal:
            return False
        
        @cache        
        def recur(target,mask):
            if target<=0:
                return False
            
            for i in range(maxChoosableInteger):
                if mask&(1<<i): 
                    continue
                if not recur(target-i-1, mask^(1<<i)):
                    return True
                
            return False
        
        ans = recur(desiredTotal, 0)
        return ans
            
            
            