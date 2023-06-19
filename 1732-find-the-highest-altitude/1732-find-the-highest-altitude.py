class Solution:
    def largestAltitude(self, a: List[int]) -> int:
        n=len(a)
        pref=[0]*(n+1)
        
        for i in range(1,n+1):
            pref[i]=pref[i-1]+a[i-1]
        
        # print(pref)
        
        return max(pref)
        