class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal<=0:
            return True
        
        if ((maxChoosableInteger)*(maxChoosableInteger+1))//2<desiredTotal:
            return False
        
        @cache
        def recur(mask,target):
            if target<=0:       ## mtlb next banda har rha h
                return 0
            
            for i in range(maxChoosableInteger):
                if not mask&(1<<i):
                    if not recur(mask^(1<<i), target-(i+1)):
                        return True
            return False
    
        ans = recur(0,desiredTotal)
        return ans