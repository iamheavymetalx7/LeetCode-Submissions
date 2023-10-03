class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        bds =[0 for _ in range(n)]
        
        m = len(requests)
        ans = [0]
        
        def recur(idx,reqs):
            if idx>=m:
                for i in range(n):
                    if bds[i]:
                        return
                ans[0]=max(ans[0],reqs)
                return
            
            recur(idx+1,reqs)
            bds[requests[idx][0]]-=1
            bds[requests[idx][1]]+=1
            recur(idx+1,reqs+1)
            bds[requests[idx][0]]+=1
            bds[requests[idx][1]]-=1


        recur(0,0)
        return ans[0]
            