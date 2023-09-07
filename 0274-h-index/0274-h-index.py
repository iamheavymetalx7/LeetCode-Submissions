class Solution:
    def hIndex(self, cite: List[int]) -> int:
        cite.sort(reverse=True)
        
        n=len(cite)
        ans=0
        
        for i in range(n):
            if cite[i]>=i+1:
                ans+=1
        return ans