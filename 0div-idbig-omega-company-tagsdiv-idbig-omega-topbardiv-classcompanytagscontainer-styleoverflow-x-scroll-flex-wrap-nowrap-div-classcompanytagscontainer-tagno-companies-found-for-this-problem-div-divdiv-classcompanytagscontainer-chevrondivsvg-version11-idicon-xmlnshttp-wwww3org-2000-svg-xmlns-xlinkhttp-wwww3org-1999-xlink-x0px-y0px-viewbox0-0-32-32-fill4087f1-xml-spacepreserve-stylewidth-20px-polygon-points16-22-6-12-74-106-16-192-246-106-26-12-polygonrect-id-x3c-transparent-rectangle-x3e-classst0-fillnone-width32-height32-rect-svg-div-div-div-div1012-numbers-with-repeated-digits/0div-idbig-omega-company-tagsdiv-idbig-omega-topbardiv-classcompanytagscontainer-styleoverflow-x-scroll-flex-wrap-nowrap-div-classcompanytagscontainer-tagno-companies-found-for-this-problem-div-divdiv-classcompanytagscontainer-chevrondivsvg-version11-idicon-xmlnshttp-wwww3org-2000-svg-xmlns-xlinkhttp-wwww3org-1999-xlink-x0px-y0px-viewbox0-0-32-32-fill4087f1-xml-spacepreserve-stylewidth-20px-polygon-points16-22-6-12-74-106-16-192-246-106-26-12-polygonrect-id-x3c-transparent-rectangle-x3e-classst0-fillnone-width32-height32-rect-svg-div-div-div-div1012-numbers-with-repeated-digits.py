class Solution:
    def numDupDigitsAtMostN(self, m: int) -> int:
        x=str(m)
        
        n =len(x)
        
        @cache
        def recur(idx,started,tight,repeat,mask):
            
            if idx>=n:
                if repeat:
                    return 1
                return 0
            
            ub = 9 if not tight else int(x[idx])
            ans =0
            
            for dig in range(ub+1):
                if dig==0 and not started:
                    ans = ans+ recur(idx+1,False,tight&(dig==ub),repeat,mask)
                else:
                    if mask&(1<<dig):
                        ans = ans+ recur(idx+1,started,tight&(dig==ub),True,mask)
                    else:
                        ans = ans+recur(idx+1,True,tight&(dig==ub),repeat,mask^(1<<dig))
            return ans
        
        val = recur(0,False,True,False,0)
        return val
                        
        
        