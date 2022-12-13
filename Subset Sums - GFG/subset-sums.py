#User function Template for python3
class Solution:
    
    def recursion(self,arr,N,ans,temp,index):
        if index>=N:
            ans.append(temp)
            return
        
        self.recursion(arr,N,ans,temp+arr[index],index+1)
        self.recursion(arr,N,ans,temp,index+1)
    
	def subsetSums(self, arr, N):
	    ans=[]
	    temp=0
	    self.recursion(arr,N,ans,temp,0)
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends