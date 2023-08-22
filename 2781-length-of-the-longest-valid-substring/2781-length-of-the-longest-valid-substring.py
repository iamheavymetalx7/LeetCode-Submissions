class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        
        forbid = set(forbidden)
        
        n=len(word)
        ans=0
        right = n-1
        
        for left in range(n-1,-1,-1):
            for k in range(left, min(left+10,right+1)):
                if word[left:k+1] in forbid:
                    right = k-1
                    break
            ans = max(ans,right-left+1)
        return ans