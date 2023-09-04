class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        arr = [i for i,x in enumerate(nums) if x]
        n=len(arr)
        pref_sum =[0]*(n)
        pref_sum[0]=arr[0]
        
        
        for i in range(1,n):
            pref_sum[i]=pref_sum[i-1]+arr[i]
        # print(pref_sum)
        ans = int(1e19)
        
        for i in range(n-k+1):
            mid = i+k//2
            right = pref_sum[i+k-1]-pref_sum[mid]
            left = (pref_sum[mid-1] if mid-1>=0 else 0)-(pref_sum[i-1] if i-1>=0 else 0)
            ans = min(ans, right-left+(arr[mid] if k%2==0 else 0))
        
        ## subtract the moves that can be saved
        r = (k-1)//2
        ans -= 2*(r*(r+1))//2 + ((r+1) if k%2==0 else 0)
        
        return ans