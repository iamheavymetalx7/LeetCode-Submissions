class Solution:
    def distinctIntegers(self, n: int) -> int:
        vis=set()
        vis.add(n)
        j=0
        while j<100:
            for ele in vis.copy():
                for i in range(1,101):
                    if ele%i==1 and i>=1 and i<=n:
                        vis.add(i)
            j+=1
        
        return len(vis)
                    
        