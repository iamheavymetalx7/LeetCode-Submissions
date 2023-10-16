class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        @cache
        def fact(x):
            if x<=1:
                return 1
            return x*fact(x-1)
        
        def ncr(n,r):
            return fact(n)//(fact(n-r)*fact(r))
        
        arr=[]
        n = rowIndex
        for idx in range(n+1):
            arr.append(ncr(n,idx))
        return arr