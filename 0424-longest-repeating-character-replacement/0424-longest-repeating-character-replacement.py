class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        n=len(s)
        l=0

        maxi=0
        for r in range(n):
            dic[s[r]]+=1


            
            while ((r-l+1 - max(dic.values()))>k):
                dic[s[l]]-=1
                if dic[s[l]]==0:
                    del dic[s[l]]

                l+=1
            
            maxi=max(maxi,r-l+1)            
        return maxi
        