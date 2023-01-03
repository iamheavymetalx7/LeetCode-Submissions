#User function Template for python3

class Solution:
    def removeStudents(self, nums, n):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        ans=n - size
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        H=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.removeStudents(H,N))
# } Driver Code Ends