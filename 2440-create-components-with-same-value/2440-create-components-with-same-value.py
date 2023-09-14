class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        summ = sum(nums)
        n=len(nums)

        
        g =[[] for _ in range(n)]
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        
        divisors =[]
        for i in range(1,int(math.sqrt(summ))+1):
            if summ%i==0:
                if i!=summ//i:
                    divisors.append(i)
                    divisors.append(summ//i)
                else:
                    divisors.append(i)
        divisors.sort()
        # print(divisors)
        ROOT = 0
        QUE =deque([ROOT])
        PARENT =[-1]*(n+1)
        PARENT[ROOT]=n
        CHILD = [[] for _ in range(n)]
        
        
        TOP_SORT = []
        
        
        
        
        while QUE:
            x = QUE.popleft()
            TOP_SORT.append(x)
            
            for to in g[x]:
                if PARENT[to]==-1:
                    PARENT[to]=x
                    CHILD[x].append(to)
                    QUE.append(to)
        
        # print(TOP_SORT,"topoo")
        
        for d in divisors:
            b = nums[:]
            ANS =0
            
            for x in TOP_SORT[::-1]:

                sc = b[x]
                
                for to in CHILD[x]:
                    sc+=b[to]
                if sc==d:
                    ANS+=1
                    b[x]=0
                else:
                    b[x]=sc
            # print(ANS*d,ANS,d,summ)
            if ANS*d == summ:
                return (ANS-1)
        return 0
                
                