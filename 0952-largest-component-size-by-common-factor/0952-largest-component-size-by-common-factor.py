
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



            

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:

        def primes_set(a):
            for i in range(2, int(math.sqrt(a))+1):
                if a % i == 0:
                    return primes_set(a//i) | set([i])
            return set([a])

            
        
        n=len(nums)
      
        uf = UnionFind(n)
        primes = defaultdict(list)
        for i in range(n):
            prime_fac = primes_set(nums[i])
            for q in prime_fac:
                primes[q].append(i)
        
        for _,indexes in primes.items():
            for i in range(len(indexes)-1):
                uf.merge(indexes[i],indexes[i+1])
        
        
        counter = defaultdict(int)
        
        for i in range(n):
            counter[uf.find(i)]+=1
        
        return max(counter.values())
        
        