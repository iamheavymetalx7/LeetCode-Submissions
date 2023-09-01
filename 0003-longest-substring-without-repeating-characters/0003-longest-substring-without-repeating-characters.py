class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## sliding window techinque
        n=len(s)
        if not s:return 0
        l=0
        dic = defaultdict(int)
        maxi =0
        for r in range(n):
            while s[r] in dic:
                dic[s[l]]-=1
                
                if dic[s[l]]==0:
                    del dic[s[l]]
                
                l+=1
                

            dic[s[r]]+=1
            r+=1
            maxi=max(r-l,maxi)
        maxi = max(r-l,maxi)

        return maxi