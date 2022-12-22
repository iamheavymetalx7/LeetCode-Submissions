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
                
                if threesum<sumo:
                    cnt+=right-left
                    left+=1
                else:
                    right-=1
                
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