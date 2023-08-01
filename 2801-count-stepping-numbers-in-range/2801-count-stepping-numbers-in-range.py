class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        

    
        low = int(low)
        low-=1

        low = str(low);high = str(high) 


        MOD = 10**9+7

        @cache
        def recur(tight,is_started,last,idx,s):
            if idx ==len(s):
                return 1

            ub= 9 if not tight else int(s[idx])

            ans =0

            for dig in range(0,ub+1):
                if is_started and abs(last-dig)!=1:
                    continue
                new_is_started = True if is_started else dig!=0
                ans = (ans+ recur((tight&(dig==ub)),new_is_started,dig,idx+1,s))%MOD
            return ans
        val1 = recur(True,False,0,0,high)%MOD
        val2 = recur(True,False,0,0,low) %MOD


        return ((val1-val2)%MOD)


