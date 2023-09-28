class Solution:
    def findIntegers(self, m: int) -> int:
        x = bin(m)[2:]
        n = len(x)
        print(x)
        
        @cache
        def recur(idx,started,tight,prev):
            if idx>=n:
                return 1
            
            ub = 1 if not tight else int(x[idx])
            
            ans = 0
            for dig in range(ub+1):
                if dig==0:
                    ans = ans+recur(idx+1,started,tight&(dig==ub),dig)
                elif dig==1 and prev!=1:
                    ans = ans+recur(idx+1,True,tight&(dig==ub),dig)
            return ans
        
        val = recur(0,False,True,0)
        return val