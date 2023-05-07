class Solution:
    def distinctDifferenceArray(self, a: List[int]) -> List[int]:

        
        
        n=len(a)
        arr=[]
        
        for i in range(n):
            arr.append(-len(Counter(a[i+1:])) +len(Counter(a[:i+1])))
            
        return arr