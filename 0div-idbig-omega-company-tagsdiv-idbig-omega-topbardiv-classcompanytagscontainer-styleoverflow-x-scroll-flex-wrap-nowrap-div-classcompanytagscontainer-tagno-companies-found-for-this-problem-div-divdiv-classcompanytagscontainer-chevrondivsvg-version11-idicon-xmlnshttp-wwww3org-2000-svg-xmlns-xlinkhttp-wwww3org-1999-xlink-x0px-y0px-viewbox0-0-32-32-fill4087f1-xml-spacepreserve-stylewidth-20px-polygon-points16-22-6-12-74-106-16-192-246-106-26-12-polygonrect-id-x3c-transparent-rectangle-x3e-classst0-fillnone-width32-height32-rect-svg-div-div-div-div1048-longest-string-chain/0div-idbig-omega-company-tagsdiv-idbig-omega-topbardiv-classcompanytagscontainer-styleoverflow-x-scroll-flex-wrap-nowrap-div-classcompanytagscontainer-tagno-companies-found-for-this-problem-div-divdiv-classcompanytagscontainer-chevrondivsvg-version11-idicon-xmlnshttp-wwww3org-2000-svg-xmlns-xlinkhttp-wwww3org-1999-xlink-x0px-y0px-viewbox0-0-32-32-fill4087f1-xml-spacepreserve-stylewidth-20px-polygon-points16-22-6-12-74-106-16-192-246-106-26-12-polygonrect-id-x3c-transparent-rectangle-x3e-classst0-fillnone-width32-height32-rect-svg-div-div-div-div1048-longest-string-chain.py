class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        wordSet = set(words)
        
        @cache
        def recur(word):
            ans =1
            
            for i in range(len(word)):
                predecessor = word[:i]+word[i+1:]
                
                if predecessor in wordSet:
                    ans=max(ans,1+recur(predecessor))
            return ans
        
        
        return max(recur(w) for w in wordSet)