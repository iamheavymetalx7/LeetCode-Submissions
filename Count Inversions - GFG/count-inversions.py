class BIT:
    def __init__(self,n):
        self.sums=[0]*(n+1)
    
    def query(self,idx):
        s=0
        while idx>0:
            s+=self.sums[idx]
            idx-=(idx&(-idx))
        
        return s
    
    def update(self,idx,d):
        while idx<len(self.sums):
            self.sums[idx]+=d
            idx+=(idx&(-idx))


class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        
        dic = {v:i for i,v in enumerate(sorted(set(arr)))}
        
        Fenwick = BIT(len(dic))
        res = 0
        
        for i in reversed(range(n)):
            res+=Fenwick.query(dic[arr[i]])
            Fenwick.update(dic[arr[i]]+1,1)
            
        return res  
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends