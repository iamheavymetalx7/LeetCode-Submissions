class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        n =len(nums)
        dp =[[-1]*(n) for _ in range(n)]
        
        
        
        def recur(left,right):
            if left == right:
                return nums[left]
            
            if dp[left][right]!=-1:
                return dp[left][right]
            
            
            dp[left][right] = max(nums[left]-recur(left+1,right), nums[right]-recur(left,right-1))
            
            return dp[left][right]
        
        ans = recur(0,n-1)
        if ans>=0:
            return True
        return False