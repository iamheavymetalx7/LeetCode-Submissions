#User function Template for python3
import math
class Solution:
    def checkPower(ob,N):
        # Code here
        if N==1:
            return 1
        
        
        for x in range(2,int(math.sqrt(N)+1)):
            y=1
            p=pow(x,y)
            while p<=N and p>0:
                if p==N:
                    return 1
                y+=1
                p=pow(x,y)
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())
        

        ob = Solution()
        print(ob.checkPower(N))
# } Driver Code Ends