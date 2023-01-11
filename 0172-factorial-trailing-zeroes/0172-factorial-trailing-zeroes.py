class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt_five=0
        k=5
        while n:
            cnt_five += n//k
            n=n//k
        
        return cnt_five
            
        