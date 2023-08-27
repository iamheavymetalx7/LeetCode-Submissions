class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        mark = defaultdict(int)
        
        for i,x in enumerate(stones):
            mark[x]=i
        
        n=len(stones)
        
        @cache
        def recur(idx,prevjump):
            # print(idx,prevjump)
            if idx==n-1:
                return True
            
            ans = False
            
            for nextJump in range(prevjump-1,prevjump+2):
                if nextJump>0 and stones[idx]+nextJump in mark:
                    newidx = mark[stones[idx]+nextJump]
                    ans |= recur(newidx,nextJump)
            
            return ans
        
        val = recur(0,0)
        return val