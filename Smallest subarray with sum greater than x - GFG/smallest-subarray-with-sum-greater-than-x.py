import math
class Solution:
    def smallestSubWithSum(self, a, n, x):
        # Your code goes here 
        summ=0
        mini = math.inf
        start=0
        
        for i in range(n):
            summ+=a[i]
            
            while summ>x:
                mini=min(mini,i-start+1)
                summ-=a[start]
                start+=1
        
        if mini==math.inf:
            return 0
        return mini
        
        
        
        
#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends