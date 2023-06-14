

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
		
		arr=[]
		for k,v in enumerate(nums):
		    arr.append([k,v])
		   
	    arr.sort(key=lambda x:x[1])
	    n=len(nums)
	    vis =[0]*(n+1)
	    cycle=0
	    
	    for i in range(n):
	        if vis[i] or arr[i][0]==i:
	            if arr[i][0]==i:
	                cycle+=1
                continue
	       
	        j=i
	       
	        while not vis[j]:
	            vis[j] = 1
	            j = arr[j][0]
	       
	        cycle+=1
	   
	    return n-cycle
	       
		
		

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends