class Solution:
    def maxArea(self, a: List[int]) -> int:
        n=len(a)
        
        l,r=0,n-1
        
        res=0
        
        while l<r:
            res=max(res,(r-l)*min(a[r],a[l]))

            if a[r]<a[l]:
                r-=1
            else:
                l+=1
        return res
        
        