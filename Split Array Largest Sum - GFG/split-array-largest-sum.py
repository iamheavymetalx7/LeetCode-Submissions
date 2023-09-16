#User function Template for python3

class Solution:
    def splitArray(self, arr, n, k):
        # code here 
        
        l=max(arr)-1
        r=sum(arr)+1
        
        def check(mid,k):
            count=0
            sum=0
            
            for i in range(n):
                if arr[i]>mid:
                    return False
                
                sum+=arr[i]
                
                if sum>mid:
                    count+=1
                    sum=arr[i]
            count+=1
            
            if count<=k:
                return True
            
            return False
        
        while r-l>1:
            mid = (l+r)//2
            if check(mid,k):
                r=mid
            else:
                l=mid
        
        return r

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
# } Driver Code Ends