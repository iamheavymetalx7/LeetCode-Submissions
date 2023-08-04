from math import *
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        cnt =0
        
        def isPrime(n):
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True

        for num in range(left,right+1):
            s = bin(num)[2:]
            c = s.count("1")
            if c==1:
                continue
            if isPrime(c):
    
                cnt+=1
        
        return cnt
            
        