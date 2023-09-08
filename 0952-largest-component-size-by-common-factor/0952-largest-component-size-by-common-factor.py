'''
the previous implementation had error in the sieve function, sieve[i]=i for all i is the correct implementation
'''
class UnionFind:
    def __init__(self,n):
        self.par=[i for i in range(n)]
        self.rank =[1 for i in range(n)]
        self.cnt = n
    def find(self,x):
        p=self.par[x]
        
        while p!=self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p=self.par[p]
        return p
    
    def merge(self,x,y):
        p1,p2 = self.find(x),self.find(y)
        
        if p1==p2:
            return True
        self.cnt-=1
        
        if self.rank[p1]>self.rank[p2]:
            self.rank[p1]+=1
            self.par[p2]=p1
        else:
            self.rank[p2]+=1
            self.par[p1]=p2
        return False



mx = 10**5
    
spf =[i for i in range(mx+1)]

for i in range(2,int(math.sqrt(mx))+1):
    if spf[i]==i:
        for j in range(i*i,mx+1,i):
            spf[j]=i


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        
        def calc_prime_facs(x):
            while x!=1:
                yield spf[x]
                x//=spf[x]
            
            
            
        
        n=len(nums)
      
        uf = UnionFind(n)
        primes = defaultdict(list)
        for i in range(n):
            
            for q in calc_prime_facs(nums[i]):
                primes[q].append(i)
        
        for _,indexes in primes.items():
            for i in range(len(indexes)-1):
                uf.merge(indexes[i],indexes[i+1])
        
        
        counter = defaultdict(int)
        
        for i in range(n):
            counter[uf.find(i)]+=1
        
        return max(counter.values())