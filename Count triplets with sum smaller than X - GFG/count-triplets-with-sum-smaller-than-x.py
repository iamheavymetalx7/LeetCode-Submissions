class Solution:
    def countTriplets(self, arr, n, sumo):
        #code here

        # distinct values all
        cnt=0
        arr.sort()
        
        for i in range(len(arr)-2):
            left=i+1
            right=len(arr)-1
            
            while left<right:
                threesum = arr[i]+arr[left]+arr[right]
                
                if threesum<sumo:  # found the triplet
      # since arr[right] >= arr[left], therefore, we can replace arr[right] by any 
      # number between left and right to get a sum less than the target sum
                    cnt+=right-left
                    left+=1
                else:
                    right-=1    # we need a pair with a smaller sum
                
        return cnt

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a=list(map(int,input().split()))
        ob = Solution()
        ans=ob.countTriplets(a,n,k)
        print(ans)
# } Driver Code Ends