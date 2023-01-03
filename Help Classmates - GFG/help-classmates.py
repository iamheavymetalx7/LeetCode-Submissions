#User function Template for python3
from collections import deque
class Solution:
    def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        stack=[]

        ans=[-1]*n

        for i in range(n-1,-1,-1):
            while stack and stack[-1]>=arr[i]:
                stack.pop()
            if len(stack)==0:
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(arr[i])
            
        return ans
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [ int(x) for x in input().split() ]
        obj = Solution()
        result = obj.help_classmate(arr,n)
        for i in result:
            print(i,end=' ')
        print()

# } Driver Code Ends