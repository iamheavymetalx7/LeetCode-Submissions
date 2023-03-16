class Solution:
    '''
    https://leetcode.com/problems/maximize-win-from-two-segments/discuss/3252701/Python-(Simple-DP-%2B-Sliding-Window)
    '''
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        # we are given k, the length of the segment and we can select only 2 segments
        # we wish to return the max number of prizes i can win
        
        
    

        
        n=len(prizePositions)
        
        left,dp,max_val=0,[0]*(n+1),0
        
        for right in range(n):
            while left<n and prizePositions[right]-prizePositions[left]>k:
                left+=1
            
            dp[right+1]=max(dp[right],right-left+1)
            # print(right,left)
            max_val=max(max_val, dp[left]+right-left+1)
        return max_val
        
        