#Your task is to complete this function
#Your should return the required output
from collections import *
class Solution:
    def maxLen(self, n, arr):
        #Code here

        mp = defaultdict(int)
        mp[0]=-1
        s =0
        ans=0
        for i in range(n):
            s+=arr[i]
            
            to_find = s-0
            if s in mp:
                ans = max(ans,i-mp[to_find])
            
            if s not in mp:
                mp[s]=i
        
        return ans
                
#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends