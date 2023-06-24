# The idea of 'last balloon to burst' is the key!
# "First of all, dp[i][j] in here means, the maximum coins we get after we burst all the balloons between i and j in the original array."

# https://leetcode.com/problems/burst-balloons/discuss/892552/For-those-who-are-not-able-to-understand-any-solution-WITH-DIAGRAM

# some easier solutions to try and dp python: https://leetcode.com/problems/burst-balloons/discuss/970727/Python-5-lines-dp-explained
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        dp = [[-1]*305 for _ in range(305)]
        
        nums=[1]+nums+[1]
        n = len(nums)
        
        def recur(i,j):
            if i>j:
                return 0
            if i==j:
                temp = nums[i]
                if i-1>=0:
                    temp*=nums[i-1]
                if i+1<n:
                    temp*=nums[i+1]
                
                return temp
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            ans=0
            
            for k in range(i,j+1):
                temp=nums[k]
                
                if j+1<n:
                    temp*=nums[j+1]
                if i-1>=0:
                    temp*=nums[i-1]
                
                temp+=recur(i,k-1)+recur(k+1,j)
                
                ans=max(ans,temp)
            dp[i][j]=ans
            
            return dp[i][j]
        
        return recur(1,len(nums)-2)