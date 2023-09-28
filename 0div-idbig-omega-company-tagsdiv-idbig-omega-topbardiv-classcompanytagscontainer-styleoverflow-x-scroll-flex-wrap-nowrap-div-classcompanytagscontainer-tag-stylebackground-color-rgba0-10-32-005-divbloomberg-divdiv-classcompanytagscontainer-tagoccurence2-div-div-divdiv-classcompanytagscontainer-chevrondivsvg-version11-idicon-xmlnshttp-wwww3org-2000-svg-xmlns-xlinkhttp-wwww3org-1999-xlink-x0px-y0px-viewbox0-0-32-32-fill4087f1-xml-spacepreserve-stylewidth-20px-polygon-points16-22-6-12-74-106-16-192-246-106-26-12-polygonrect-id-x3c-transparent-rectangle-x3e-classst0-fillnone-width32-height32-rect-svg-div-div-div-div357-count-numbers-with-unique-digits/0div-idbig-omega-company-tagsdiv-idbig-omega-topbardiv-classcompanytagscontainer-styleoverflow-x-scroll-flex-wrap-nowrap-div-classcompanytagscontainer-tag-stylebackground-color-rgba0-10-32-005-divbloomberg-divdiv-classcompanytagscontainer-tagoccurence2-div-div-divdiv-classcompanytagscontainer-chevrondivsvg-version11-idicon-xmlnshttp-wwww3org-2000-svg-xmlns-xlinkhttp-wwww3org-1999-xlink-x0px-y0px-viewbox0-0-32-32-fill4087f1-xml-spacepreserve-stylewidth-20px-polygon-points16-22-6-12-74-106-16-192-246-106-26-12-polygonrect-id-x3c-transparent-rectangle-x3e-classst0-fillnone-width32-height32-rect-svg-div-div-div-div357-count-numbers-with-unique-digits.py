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
                
                new_started = True if started else dig!=0
                if started and mask&(1<<dig):
                    continue
                new_mask = 0 if not new_started else mask^(1<<dig)
                ans = (ans+recur(idx+1,tight&(dig==ub),new_started,new_mask))
            return ans
        
        val = recur(0,True,False,0)
        return (val)