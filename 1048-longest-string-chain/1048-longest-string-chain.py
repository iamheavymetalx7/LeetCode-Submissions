class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        n=len(words)
        dp=[1]*(n)
        words.sort(key=len)

        
        def compare(s1,s2):
            if len(s1)!=len(s2)+1:
                return False
            
            first,second=0,0
            
            while first<len(s1):
                if second<len(s2) and  s1[first]==s2[second]:
                    first+=1
                    second+=1
                else:
                    first+=1
            
            if len(s1)==first and len(s2)==second:
                return True
            
            return False
        
        length=1
        for idx in range(1,n):
            for prev in range(idx):
                if compare(words[idx],words[prev]) and dp[idx]<1+dp[prev]:
                    dp[idx]=1+dp[prev]
    
        return max(dp)
                
                
        