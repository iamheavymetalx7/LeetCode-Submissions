class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans =[]
        
        def recur(x,arr):
            if x>n+1:
                return
            if len(arr)==k:
                ans.append(deepcopy(arr))
                return
            
            for i in range(n):
                arr.append(x+i)
                recur(x+i+1,arr)
                arr.pop()
        recur(1,[])
        
        return (ans)