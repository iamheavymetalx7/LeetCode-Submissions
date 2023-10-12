class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        
        res=0
        for i in range(k):
            res += cardPoints[i]
        
        curr = res
        
        for j in range(k-1,-1,-1):
            curr -= cardPoints[j]
            curr += cardPoints[n-k+j]
            res = max(res,curr)
        return res