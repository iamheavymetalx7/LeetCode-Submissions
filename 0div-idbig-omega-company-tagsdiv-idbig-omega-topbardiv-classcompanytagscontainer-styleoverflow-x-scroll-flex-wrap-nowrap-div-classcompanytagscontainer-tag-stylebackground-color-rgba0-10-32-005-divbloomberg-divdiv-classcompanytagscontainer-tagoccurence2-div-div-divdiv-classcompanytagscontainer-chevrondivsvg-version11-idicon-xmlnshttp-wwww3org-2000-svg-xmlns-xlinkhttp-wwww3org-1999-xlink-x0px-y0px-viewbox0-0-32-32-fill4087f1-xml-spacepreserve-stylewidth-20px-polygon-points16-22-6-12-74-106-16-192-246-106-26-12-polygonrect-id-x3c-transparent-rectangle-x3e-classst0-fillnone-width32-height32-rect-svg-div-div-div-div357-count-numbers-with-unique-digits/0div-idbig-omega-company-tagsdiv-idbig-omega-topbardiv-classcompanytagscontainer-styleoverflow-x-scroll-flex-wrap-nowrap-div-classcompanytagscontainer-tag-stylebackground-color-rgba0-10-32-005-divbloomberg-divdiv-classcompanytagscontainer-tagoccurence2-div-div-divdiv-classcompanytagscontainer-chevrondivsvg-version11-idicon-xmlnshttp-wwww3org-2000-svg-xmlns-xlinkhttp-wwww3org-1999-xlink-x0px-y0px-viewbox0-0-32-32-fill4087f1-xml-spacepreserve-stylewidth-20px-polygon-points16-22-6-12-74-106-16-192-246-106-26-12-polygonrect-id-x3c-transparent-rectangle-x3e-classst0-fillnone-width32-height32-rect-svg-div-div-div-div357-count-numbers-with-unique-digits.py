class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        

        x = pow(10,n)
        x-=1
        x = str(x)
        n=len(x)

        @cache
        def recur(idx,tight,started,mask):
            if idx>=n:
                return 1
            
            
            ub = 9 if not tight else int(x[idx])
            ans=0
            for dig in range(0,ub+1):
                
                if dig==0 and not started:
                    ans=(ans+recur(idx+1,tight&(dig==ub),False,mask))
                
                else:
                    if mask&(1<<dig):
                        continue
                    else:
                        ans = (ans+ recur(idx+1,tight&(dig==ub),True,mask^(1<<dig)))
            return ans
        val = recur(0,True,False,0)
        return val          