class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        pref = [0]*n
        
        pref[0]=nums[0]
        
        for i in range(1,n):
            pref[i]=pref[i-1]+nums[i]
        
        # print(pref)
        
        ans=[-1]*(n)
        
        for i in range(n):
            if i-k<0 or i+k>=n:
                continue
            elif i-k==0:
                ans[i] = pref[i+k]//(2*k+1)
            else:
                ans[i] = (pref[i+k]-pref[i-k-1])//(2*k+1)
        return ans     
        
        
        