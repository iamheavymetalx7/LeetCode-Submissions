class Solution:
    def minOperations(self, n: int) -> int:
        
        ans =0 
        
        if n%2:
            for i in range(n//2):
                ans+=2*(n//2-i)
        else:
            for i in range(1,n//2+1):
                ans+=1+2*(n//2-i)
        return ans