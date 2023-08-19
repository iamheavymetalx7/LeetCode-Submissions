class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        
        
        @cache
        def recur(tight,is_started,odd,even,n,rem,nums):

            if n==len(nums):
                if (rem==0 and is_started and odd==even):
                    return 1
                else:
                    return 0
   
            
            ub = 9 if not tight else int(nums[n])
            ans=0
            for dig in range(ub+1):
                new_is_started = is_started | dig!=0
                new_odd = odd+(new_is_started&(dig%2!=0))
                new_even = even+(new_is_started&(dig%2==0))
                new_rem = (rem*10+dig)%k
                ans+=recur(tight&(dig==ub),new_is_started,new_odd,new_even,n+1,new_rem,nums)
            return ans
        
        
        low-=1
        
        highh = str(high)
        loww= str(low)
        
        val1 = recur(True,False,0,0,0,0,highh)
        
        val2 = recur(True,False,0,0,0,0,loww)
        
        
        return val1-val2
        