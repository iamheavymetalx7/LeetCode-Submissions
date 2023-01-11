class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        
        is_prime=[1]*(n+1)
        is_prime[0]=0
        is_prime[1]=0
        
        for i in range(2,n+1):
            if i*i>n:
                break
            if is_prime[i]:
                for j in range(i*i,n+1,i):
                    is_prime[j]=0
        cnt=0
        for i in range(len(is_prime)-1):
            if is_prime[i]:
                cnt+=1
            
        return cnt