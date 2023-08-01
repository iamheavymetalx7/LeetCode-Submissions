from functools import cache
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:

        # /**
# * author:Hisoka-TheMagician
# * created: 01/08/2023 13:37 Chennai, India
# **/
        

        num1 =int(num1)
        num1-=1
        num1=str(num1)
        MOD = int(1e9)+7

        maxi =0
        
        @cache
        def recur(tight,idx,curr,s):
            nonlocal maxi

            if idx==len(s):
                maxi = max(maxi,curr)
                return min_sum<=curr<=max_sum


            ub  = 9 if not tight else int(s[idx])
            ans = 0
            for dig in range(0,ub+1):

                ans =(ans + recur(tight&(dig==ub),idx+1,curr+dig,s))%MOD

            return ans
        ans = recur(True,0,0,num2)%MOD

        ans2 = recur(True,0,0,num1)%MOD

        return ((ans-ans2)%MOD)























































        
       
            
                
        




