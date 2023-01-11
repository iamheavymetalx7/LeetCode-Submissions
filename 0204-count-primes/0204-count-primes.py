# time complexity : O(n*log(log(n)))
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
            if is_prime[i] and i*i<=n:
                for j in range(i*i,n+1,i):
                    is_prime[j]=0
        # print(is_prime)     
        cnt=0        
        for j in range(len(is_prime)-1):
            if is_prime[j]:
                cnt+=1
                
        return cnt