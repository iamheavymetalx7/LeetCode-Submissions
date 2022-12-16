class Solution:
    ## Similar to longest common substring!!
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        m=len(nums2)
        
        dp=[[-1]*(m+1) for i in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=0
        for j in range(m+1):
            dp[0][j]=0
        ans = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                    ans=max(ans,dp[i][j])
                else:
                    dp[i][j]=0
        return ans
        