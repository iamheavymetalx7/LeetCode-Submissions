class Solution:
    def generate(self, n: int) -> List[List[int]]:
        
        if n==1:
            return [[1]]

        if n==2:
            return [[1],[1,1]]
        
        arr =[[1],[1,1]]
        
        def recur(i):
            if i<=0:
                return 
            ans = arr[-1]
            new=[1]
            for j in range(len(ans)-1):
                new.append(ans[j]+ans[j+1])
            new.append(1)
            arr.append(new)
            recur(i-1)
            
        recur(n-2)
        return arr
            
            