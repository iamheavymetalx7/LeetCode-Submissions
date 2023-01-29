class Solution:
    def monkeyMove(self, n: int) -> int:
        mod=10**9+7
        
        # use fermat's theorem: a^(p-1) = a mod p
        ans = pow(2,n,mod)
        ans=ans-2
        if ans==-1:
            return 1000000006
        return ans
        