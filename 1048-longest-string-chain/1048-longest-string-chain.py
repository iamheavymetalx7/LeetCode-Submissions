## Time Complexity ; O(N^2*L + N log(N)), where O(N^2) -- two for loops and O(L) -- checkPossible
class Solution:
    def checkPossible(self,s1,s2):
        if len(s1)!=len(s2)+1: return False
        
        first=0
        second=0
        
        while first<len(s1):
            if second<len(s2) and s1[first]==s2[second]:
                first+=1 
                second+=1
            else:
                first+=1
        if first==len(s1) and second==len(s2):
            return True
        
        return False
    
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        n=len(words)
        maxi=1
        dp=[1]*n
        
        print(words)
                
        for i in range(0,n):
            for prev in range(i):
                if dp[i]<dp[prev]+1 and self.checkPossible(words[i],words[prev]):
                    dp[i] = dp[prev]+1
                    
            if dp[i]>maxi:        
                maxi=dp[i]
            
        return maxi