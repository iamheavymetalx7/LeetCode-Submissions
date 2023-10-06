class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n=len(arr)
        pref =[0 for _ in range(n)]
        suff = [0 for _ in range(n)]
        
        pref[0]=1
        suff[-1]=1
        
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                pref[i]=1+pref[i-1]
            else:
                pref[i]=1
        
        for k in range(n-2,-1,-1):
            if arr[k]>arr[k+1]:
                suff[k]=1+suff[k+1]
            else:
                suff[k]=1
        
        print(pref,suff)
        maxi=0
        for i in range(n):
            if pref[i]-1==0 or suff[i]-1==0:
                continue
            maxi = max(maxi,pref[i]+suff[i]-1)
        return maxi if maxi>=3 else 0