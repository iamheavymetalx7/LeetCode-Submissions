class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        a=[[] for _ in range(n+1)]
        
        for i in range(n):
            a[nums[i]].append(i)
        # print(a)
        
        ans = 0
        
        for arr in a:
            if not arr:
                continue
            
            l=0
            r=0
        
            x=len(arr)
            while l<x:
                
                while r+1<x and ((arr[r+1]-arr[l])-(r-l+1))<=k:
                    r+=1
                
                ans=max(ans,r-l+1)
                l+=1
        return ans