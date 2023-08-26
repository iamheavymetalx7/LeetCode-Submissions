class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        # print(pairs)
        n=len(pairs)
        
        @cache
        def recur(idx,prev):
            if idx>=n:
                return 0
            
            ans = 0
            
            ##take case
            if prev==-1 or pairs[prev][1]<pairs[idx][0]:
                ans =max(ans,1+recur(idx+1,idx))
            
            # nottake case
            ans = max(ans, recur(idx+1,prev))
            
            return ans
        val = recur(0,-1)
        return val