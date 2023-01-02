#User function Template for python3
class Solution:
    def findKRotation(self,nums,  n):
        # code here
        low=0
        high=len(nums)-1
        
        while low<=high:
            mid=(low+high)//2
            
            prev = (mid-1+n)%n
            nex=(mid+1)%n
            
            if nums[prev]>=nums[mid] and nums[mid]<=nums[nex]:
                return mid
            elif nums[mid]<=nums[high]:
                high=mid-1
            elif nums[mid]>=nums[low]:
                low=mid+1
        return 0
                
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends