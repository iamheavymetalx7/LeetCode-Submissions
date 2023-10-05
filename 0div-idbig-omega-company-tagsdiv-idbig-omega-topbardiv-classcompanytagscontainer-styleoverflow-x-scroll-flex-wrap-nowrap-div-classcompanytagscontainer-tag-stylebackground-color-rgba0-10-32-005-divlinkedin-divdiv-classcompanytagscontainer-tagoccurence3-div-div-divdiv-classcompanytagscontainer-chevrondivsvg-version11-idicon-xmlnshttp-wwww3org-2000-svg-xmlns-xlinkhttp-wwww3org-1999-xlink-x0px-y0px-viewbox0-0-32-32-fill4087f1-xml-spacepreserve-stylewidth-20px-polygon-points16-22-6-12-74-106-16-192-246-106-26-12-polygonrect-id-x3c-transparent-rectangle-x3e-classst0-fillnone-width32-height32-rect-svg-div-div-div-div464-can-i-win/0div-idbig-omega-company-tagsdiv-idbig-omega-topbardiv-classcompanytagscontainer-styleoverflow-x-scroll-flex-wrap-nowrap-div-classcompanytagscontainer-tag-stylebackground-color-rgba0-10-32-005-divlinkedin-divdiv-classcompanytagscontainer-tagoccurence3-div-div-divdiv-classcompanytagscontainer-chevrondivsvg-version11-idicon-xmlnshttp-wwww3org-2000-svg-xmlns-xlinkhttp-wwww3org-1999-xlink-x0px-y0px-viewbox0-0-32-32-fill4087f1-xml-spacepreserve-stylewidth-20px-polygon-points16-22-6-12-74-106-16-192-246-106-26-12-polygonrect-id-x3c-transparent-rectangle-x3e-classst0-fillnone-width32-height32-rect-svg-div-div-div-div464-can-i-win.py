class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal<=0:
            return True
        
        if ((maxChoosableInteger)*(maxChoosableInteger+1))//2<desiredTotal:
            return False
        
        @cache
        def recur(mask,tgt):
            if tgt<=0:
                return False
            
            for i in range(maxChoosableInteger):
                if not (mask&(1<<i)):
                    if not recur(mask^(1<<i),tgt-(i+1)):
                        return True
            return False
        
        return recur(0,desiredTotal)