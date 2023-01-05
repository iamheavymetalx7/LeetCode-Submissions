class Solution:
    def frequencySort(self, s: str) -> str:
        
        n=len(s)
        
        from collections import Counter
        
        c=Counter(s)
        
        print(c)
        
        pq=[]
        from heapq import heapify, heappop, heappush
        
        for ele in c:
            heappush(pq,[-c[ele],ele])
            
        string =""
        
        while pq:
            count,alph = heappop(pq)
            string+=(-1*count)*alph
            
        return string
        