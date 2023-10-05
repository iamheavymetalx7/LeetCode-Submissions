class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        if sorted(A)==A:
            return []
        
        res,n=[],len(A)
        for x in range(n,0,-1):
            pl = A.index(x)
            if pl==x-1:continue
            if pl!=0:
                res.append(pl+1)
                A[:pl+1] = A[:pl+1][::-1]
            res.append(x)
            A[:x] = A[:x][::-1]
        return res
            