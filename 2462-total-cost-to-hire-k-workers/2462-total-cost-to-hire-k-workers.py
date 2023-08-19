class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n=len(costs)
        start_idx =0
        end_idx =0
        
        st=costs[:candidates]
        en=costs[max(candidates,n-candidates):]
        heapify(st)
        heapify(en)
        
        next_st,next_en = candidates, n-candidates-1
        ans=0
        
        for _ in range(k):
            ## if end is over or st is remaining and element equal at top but we need t                take element in smaller index 
            if not en or (st and st[0]<=en[0]):
                ans+=heappop(st)
                
                if next_st<=next_en:
                    heappush(st,costs[next_st])
                    next_st+=1
            else:
                ans+=heappop(en)
                
                if next_st<=next_en:
                    heappush(en,costs[next_en])
                    next_en-=1
        return ans
                