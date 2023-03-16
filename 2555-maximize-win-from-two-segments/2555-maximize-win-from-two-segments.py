class Solution:
    '''
    https://leetcode.com/problems/maximize-win-from-two-segments/discuss/3252701/Python-(Simple-DP-%2B-Sliding-Window)
    '''
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        # we are given k, the length of the segment and we can select only 2 segments
        # we wish to return the max number of prizes i can win
        
        
    
        mini = prizePositions[0]
        maxi=prizePositions[-1]
        
        n=len(prizePositions)

        if mini+2*k>=maxi:
            return n

        if k==0:
            return 2
        
        left,dp,max_val=0,[0]*(n+1),0
        
        for right in range(n):
            while left<n and prizePositions[right]-prizePositions[left]>k:
                left+=1
            
            dp[right+1]=max(dp[right],right-left+1)
            
            max_val=max(max_val, dp[left]+right-left+1)
        
        return max_val
        
        