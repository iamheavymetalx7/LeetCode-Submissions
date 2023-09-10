# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/discuss/516933/C%2B%2BPython-1-line-Simple-permutation-with-explanation
class Solution:
    def countOrders(self, n: int) -> int:
        fac=1
        prod=1
        MOD = int(1e9)+7
        for i in range(1,n+1):
            fac*=i
            fac%=MOD
        
        for j in range(1,2*n,2):
            prod*=j
            prod%=MOD
        
        
        return (prod*fac)%MOD