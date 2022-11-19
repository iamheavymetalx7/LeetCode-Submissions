#User function Template for python3
'''
Trial:
 class Solution:
    def recursion(self,i,n,nums,prev,dic):
        if i>=n:
            return 0
        if i not in dic:
            if prev==-float('inf') or nums[prev]<nums[i]:
                ans1=1+self.recursion(i+1,n,nums,i,dic)
                ans2=self.recursion(i+1,n,nums,prev,dic)
                dic[i]= max(ans1,ans2)
            else:
                dic[i]=self.recursion(i+1,n,nums,prev,dic)
        return dic[i]
            
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dic={}
        return self.recursion(0,n,nums,-float('inf'),dic)
        

'''


class Solution:
    
    
    def recursion(self,prev,a,n,i,dic):
        if i>=n:
            return 0
        ans=0
        if i not in dic:
            for j in range(i,n):
                if a[j]>prev:
                    ans=max(ans,1+self.recursion(a[j],a,n,j+1,dic))
            dic[i]=ans
        return dic[i]
            
        
    def longestSubsequence(self,a,n):
        # code here
        dic={}
        return self.recursion(-float('inf'),a,n,0,dic)
       



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends