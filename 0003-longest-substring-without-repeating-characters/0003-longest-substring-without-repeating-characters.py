class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n=len(s)
        dic = defaultdict(int)
        maxi=0
        l=0
        for r in range(n):
            # print(l,r,dic)
            while l<=r and s[r] in dic:
                dic[s[l]]-=1
            
                
                if dic[s[l]]==0:
                    del dic[s[l]]
                l+=1
                    
            dic[s[r]]+=1
            maxi=max(r-l+1,maxi)
        
        return maxi
                
        