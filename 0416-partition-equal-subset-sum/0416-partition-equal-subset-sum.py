'''
This is the variation of the knapsack problem.
Mostly we are doing the same thing as we did there,
just than instead of taking max we are doing OR to get the
boolean value.


class Solution:
    def solve(self,nums,i,dic,W):
        if W==0:
            return True
        if i>=len(nums):
            return False
        if (i,W) not in dic:
            if nums[i]>W:
                dic[(i,W)] = self.solve(nums,i+1,dic,W)
            else:
                dic[(i,W)]= self.solve(nums,i+1,dic,W-nums[i]) or self.solve(nums,i+1,dic,W)
        return dic[(i,W)]
        
                
    def canPartition(self, nums: List[int]) -> bool:
        summ=sum(nums)
        if summ%2:
            return False
        W=summ//2
        
        return self.solve(nums,0,{},W)
    
    
    https://leetcode.com/problems/partition-equal-subset-sum/discuss/2531030/Python-O(NM)-O(M)
    https://leetcode.com/problems/partition-equal-subset-sum/discuss/2674523/Python-DFS-with-Explanation
'''



class Solution:
    def recursion(self,nums,dp,W, index):
        if W==0:
            return 1

        n=len(nums)        
        if n==0 or index>=n:
            return 0
        
        if dp[index][W]==-1:
            if nums[index]<=W:
                if self.recursion(nums,dp,W-nums[index],index+1)==1:
                    dp[index][W]=1
                    return 1
            dp[index][W] = self.recursion(nums,dp,W,index+1)
        
        return dp[index][W]

    def canPartition(self, nums: List[int]) -> bool:
        summ=sum(nums)
        
        if summ%2!=0:
            return False
        
        dp=[[-1 for i in range(int(summ/2)+1)]for j in range(len(nums))]
        W=summ//2
        
        return True if self.recursion(nums,dp,W,0)==1 else False
        