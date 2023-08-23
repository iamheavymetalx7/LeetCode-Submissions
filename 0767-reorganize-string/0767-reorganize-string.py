class Solution:
    def reorganizeString(self, s: str) -> str:
        
        cf = Counter(s)
        heap =[]
        
        string=""
        
        for k,v in cf.items():
            heappush(heap,[-v,k])
        
        while heap:
            onev,onek  = heappop(heap)
            if not string or string[-1]!=onek:
                string+=onek
                if onev+1:
                    heappush(heap,[onev+1,onek])
            else:
                if not heap:
                    return ""
                else:
                    twov,twok=heappop(heap)
                    string+=twok
                    if twov+1:
                        heappush(heap,[twov+1,twok])
                    heappush(heap,[onev,onek])
        return string