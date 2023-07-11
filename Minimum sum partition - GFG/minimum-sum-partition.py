'''
## we dont calc two sets separately, think suppose i have set1, what is the sum of set 2?
## it is totalsum-s1
## and we wish to find the abs(sum(set1)-sum(set2)) = abs(total-2*sum(set1))
##so we use recursion to generate all the subsets set1, and then use above idea to find the solution
class Solution:
    def recurse(self,i,arr,s1,n,dp,totalsum):
        if i==n:
            s2=totalsum-s1
            
            difference = abs(totalsum-2*s1)
            
            return difference
            
            
        if (i,s1) not in dp:
            take = self.recurse(i+1,arr,s1+arr[i],n,dp,totalsum)
            nottake = self.recurse(i+1,arr,s1,n,dp,totalsum)
            
            dp[(i,s1)]=min(take, nottake)
        return dp[(i,s1)]            
	def minDifference(self, arr, n):
		# code here
        totalsum=sum(arr)
        s1=0
        dp={}
        return self.recurse(0,arr,s1,n,dp,totalsum)
'''


# class Solution:
    
#     def recursion(self,dp,arr,index,sum1,sum2):
#         if index>=len(arr):
#             return abs(sum1-sum2)
        
#         if dp[index][sum1]==-1:
#             diff1 = self.recursion(dp,arr,index+1,sum1+arr[index],sum2)
            
#             diff2 = self.recursion(dp,arr,index+1,sum1,sum2+arr[index])
            
#             dp[index][sum1]=min(diff1,diff2)
        
#         return dp[index][sum1]
    
    
# 	def minDifference(self, arr, n):
		# code here
# 		s=sum(arr)
# 		dp=[[-1 for i in range(s+1)] for j in range(n)]
		
# 		return self.recursion(dp,arr,0,0,0)

class Solution:
    def minDifference(self,a,n):
        
        k=sum(a)
        n=len(a)
        dp=[[0]*(k+1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0]=True

        if a[0]<=k:
            dp[0][a[0]]=True
            
        for i in range(1,n):
            for target in range(1,k+1):
                nottake = dp[i-1][target]
                
                take=False
                
                if a[i]<=target:
                    take = dp[i-1][target-a[i]]
                
                dp[i][target] = take or nottake
                
                
        mini=10**9
        
        # # print(dp)
        # idx=-1
        
        # print(dp[-1])
        
        
        for s1 in range(k//2 + 1):
            if dp[n-1][s1]:
                mini=min(mini, abs(k-s1-s1))
        # print(i)
        return mini





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends