class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        cnt=0
        for i in range(k):
            if s[i] in vowels:
                cnt+=1
        
        n=len(s)
        maxi=cnt
        # print(maxi)
        for i in range(k,n):
            # print(i,"lalala")
            if s[i-k] in vowels:
                cnt-=1
            
            if s[i] in vowels:
                cnt+=1
            
            maxi=max(maxi,cnt)
        
        return maxi
        
        