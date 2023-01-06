

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
        
        arr=[]
        ans=0
        
        for k,v in enumerate(nums):
            arr.append([k,v])
            
        arr.sort(key=lambda x:x[1])
        # print(arr)
        
        vis=[0]*(n+1)
        
        for i in range(len(nums)):
            if vis[i] or arr[i][0]==i:
                continue
            
            
            j=i
            cycle_size=0
            
            while not vis[j]:
                vis[j]=1
                j=arr[j][0]
                cycle_size+=1
            
            if cycle_size>0:
                ans+=cycle_size-1
                
        return ans
        

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