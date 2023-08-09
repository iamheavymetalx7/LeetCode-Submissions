class Solution:
    def reorganizeString(self, s: str) -> str:
        
        cf = Counter(s)
        
        heap =[]
        
        for k,v in cf.items():
            heappush(heap,[-v,k])
        
        
        ans=[]
        
        while heap:
            first_cnt, first_char = heappop(heap)
            
            if not ans or ans[-1]!=first_char:
                ans.append(first_char)
                if first_cnt+1!=0:
                    heappush(heap,[first_cnt+1,first_char])
            else:
                if not heap:
                    return ""
                else:
                    second_cnt, second_char = heappop(heap)
                    ans.append(second_char)
                    if second_cnt+1!=0:
                        heappush(heap,[second_cnt+1,second_char])
                heappush(heap,[first_cnt, first_char])
        
        return ''.join(ans)
                