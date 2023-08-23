class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap =[]
        if a:
            heappush(heap,[-a,"a"])
        if b:
            heappush(heap,[-b,"b"])
        if c:
            heappush(heap,[-c,"c"])
        
        ans =[]
        print(heap)
        while heap:
            cnt,ele = heappop(heap)
            # print(cnt,ele)
            if not ans or len(ans)>=2 and ans[-2]!=ele or ans[-1]!=ele :
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
                # print(cnt2,ele2,"else")
                # if abs(cnt2)>=2:
                #     ans+=[ele2,ele2]
                #     if cnt2+2:
                #         heappush(heap,[cnt2+2,ele2])
                if abs(cnt2)>=1:
                    ans+=[ele2]
                    if cnt2+1:
                        heappush(heap,[cnt2+1,ele2])
                heappush(heap,[cnt,ele])
        return ''.join(ans)
                