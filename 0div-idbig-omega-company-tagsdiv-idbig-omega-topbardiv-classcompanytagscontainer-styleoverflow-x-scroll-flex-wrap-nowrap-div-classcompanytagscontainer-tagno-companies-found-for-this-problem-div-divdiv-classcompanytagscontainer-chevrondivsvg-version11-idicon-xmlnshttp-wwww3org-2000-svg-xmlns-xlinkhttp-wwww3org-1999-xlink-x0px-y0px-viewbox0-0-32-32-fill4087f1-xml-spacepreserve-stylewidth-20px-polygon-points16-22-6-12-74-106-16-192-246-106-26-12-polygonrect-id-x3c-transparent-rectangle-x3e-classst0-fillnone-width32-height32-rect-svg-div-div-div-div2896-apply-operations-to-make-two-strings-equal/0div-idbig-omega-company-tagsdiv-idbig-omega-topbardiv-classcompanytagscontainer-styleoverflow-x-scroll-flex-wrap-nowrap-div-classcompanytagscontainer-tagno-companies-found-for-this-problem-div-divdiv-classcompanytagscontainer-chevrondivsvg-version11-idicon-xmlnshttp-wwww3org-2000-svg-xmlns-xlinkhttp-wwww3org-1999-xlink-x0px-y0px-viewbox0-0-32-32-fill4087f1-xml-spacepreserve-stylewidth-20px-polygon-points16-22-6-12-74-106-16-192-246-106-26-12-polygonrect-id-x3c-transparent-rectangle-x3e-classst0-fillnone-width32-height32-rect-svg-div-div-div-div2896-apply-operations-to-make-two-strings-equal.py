class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        inf = int(1e19)
        n=len(s1)

        @cache
        def recur(ind,nxt_flip,far_flip):
            if ind==n:
                if nxt_flip==0 and far_flip ==0:
                    return 0
                return inf
            ans = inf
            
            if nxt_flip:
                flip_required = (s1[ind]==s2[ind])
            else:
                flip_required = (s1[ind]!=s2[ind])
            
            if not flip_required:
                ans = min(ans, recur(ind+1,0,far_flip))
            else:
                ans = min(ans, (x if far_flip else 0)+recur(ind+1,0,far_flip^1))
                ans = min(ans,1+recur(ind+1,1,far_flip))
            return ans
        
        val = recur(0,0,0)
        if val == inf:
            return -1
        return val