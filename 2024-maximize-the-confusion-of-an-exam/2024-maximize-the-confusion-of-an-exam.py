class Solution:
    def maxConsecutiveAnswers(self, a: str, k: int) -> int:
        
        
        dic=defaultdict(int)
        n=len(a)
        l,ans=0,0
        for r in range(n):
            dic[a[r]]+=1
            
            while len(dic)>1 and r-l+1-max(dic.values())>k:
                dic[a[l]]-=1
                if dic[a[l]]==0:
                    del dic[a[l]]
                
                l+=1
            
            ans=max(r-l+1,ans)
        
        return ans