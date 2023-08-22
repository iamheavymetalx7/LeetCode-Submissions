nmax=10**5
primes = []
sieve = [1,1]+[1 for _ in range(nmax+1)]

for i in range(2,int(math.sqrt(nmax))+1):
    if sieve[i]==1:
        sieve[i]=max(i,sieve[i])
        for j in range(i,nmax,i):     ##this step of i**2 is important
            sieve[j] = max(sieve[j],i)

for i in range(nmax+1):
    if sieve[i]==1:
        sieve[i]=i

print(sieve[11047])
# print(len(primes))
# print(sieve)

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n=len(nums)
        scores= [0 for _ in range(n)]

        def calc_score(x):
            res= 0
            # print(x,"hehehhe")
            while x!=1:
                div = sieve[x]
                # print("divisor",div)
                
                while x%div==0:
                    x=x//div
                res+=1
            return res
        
        for i,ele in enumerate(nums):
            scores[i] = calc_score(ele)
            
        print(scores)
        
        prev_bigger =[-1 for _ in range(n)]
        next_bigger = [n for _ in range(n)]

            
        st=[]
        for i in range(n):
            while st and scores[st[-1]]<scores[i]:
                top=st.pop()
                next_bigger[top]=i
            st.append(i)
        
        st=[]
        for i in range(n):
            while st and scores[st[-1]]<scores[i]:
                st.pop()
            prev_bigger[i] = st[-1] if st else -1
            st.append(i)
                
            
        print(prev_bigger,"prev_smaller")
        print(next_bigger)
        
        arr=[]
        for i in range(n):
            possible = (i-prev_bigger[i])*(next_bigger[i]-i)

            arr.append((nums[i],possible))
            
        mod = int(1e9)+7
        result = 1
        arr.sort(reverse=True)
        print(arr)
        
        for num,freq in arr:
            if k==0:
                break
            take = min(freq,k)
            k-=take
            result  = result*pow(num,take,mod)
            result%=mod
        return result
            
            
            
        