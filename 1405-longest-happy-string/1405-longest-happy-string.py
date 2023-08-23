class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap =[]
        
        heappush(heap,[-a,"a"])
        heappush(heap,[-b,"b"])
        heappush(heap,[-c,"c"])
        
        ans =[]
        print(heap)
        while heap:
            cnt,ele = heappop(heap)
            if not ans or ans[-2::]!=[ele,ele] :
                if abs(cnt)>=2:
                    ans+=[ele,ele]
                    if cnt+2:
                        heappush(heap,[cnt+2,ele])
                elif abs(cnt)>=1:
                    ans+=[ele]
                    if cnt+1:
                        heappush(heap,[cnt+1,ele])                
                
            else:
                if not heap:
                    continue
                cnt2,ele2 = heappop(heap)

                if abs(cnt2)>=1:
                    ans+=[ele2]
                    if cnt2+1:
                        heappush(heap,[cnt2+1,ele2])
                heappush(heap,[cnt,ele])
        return ''.join(ans)
                