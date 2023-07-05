class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        n=len(s)
        l=0

        print(k)
        maxi=0
        for r in range(n):
            dic[s[r]]+=1
            print(dic,len(dic),r-l+1-max(dic.values()))


            
            while (len(dic)>k+1) or ((r-l+1 - max(dic.values()))>k):
                dic[s[l]]-=1
                if dic[s[l]]==0:
                    del dic[s[l]]

                l+=1
            to_add = min(k,r-l+1-max(dic.values()))
            curr = max(dic.values())+to_add
            maxi=max(maxi,curr)            
        return maxi
        