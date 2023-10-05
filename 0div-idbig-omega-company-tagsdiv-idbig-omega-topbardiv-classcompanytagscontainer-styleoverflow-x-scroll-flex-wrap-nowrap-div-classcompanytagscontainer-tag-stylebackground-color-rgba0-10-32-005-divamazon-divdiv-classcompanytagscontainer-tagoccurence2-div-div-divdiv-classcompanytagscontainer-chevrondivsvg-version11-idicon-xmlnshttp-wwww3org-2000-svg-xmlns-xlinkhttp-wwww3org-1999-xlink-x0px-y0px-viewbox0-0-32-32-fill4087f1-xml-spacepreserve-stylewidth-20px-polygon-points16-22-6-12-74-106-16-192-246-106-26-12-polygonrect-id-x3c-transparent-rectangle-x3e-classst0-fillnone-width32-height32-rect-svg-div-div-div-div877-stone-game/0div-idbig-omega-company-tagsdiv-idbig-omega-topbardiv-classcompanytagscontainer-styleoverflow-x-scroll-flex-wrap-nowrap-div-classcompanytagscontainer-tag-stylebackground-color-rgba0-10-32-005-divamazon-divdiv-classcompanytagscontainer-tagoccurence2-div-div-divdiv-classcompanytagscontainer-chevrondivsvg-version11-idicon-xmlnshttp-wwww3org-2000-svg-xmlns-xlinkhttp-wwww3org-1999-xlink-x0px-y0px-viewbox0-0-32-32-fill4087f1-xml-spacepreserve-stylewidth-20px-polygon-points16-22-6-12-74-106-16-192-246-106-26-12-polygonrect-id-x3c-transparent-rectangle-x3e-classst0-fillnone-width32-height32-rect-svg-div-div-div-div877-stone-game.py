class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        n =len(piles)
        
        @cache
        def recur(i,j):
            if i>j:
                return 0
            score=0
            score = max(piles[i]-recur(i+1,j),piles[j]-recur(i,j-1))
            
            return score
        
        ans = recur(0,n-1)
        if ans>=0:
            return True
        return False