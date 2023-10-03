class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        
        m = len(requests)
        x=(1<<m)

        maxi=0
        for i in range(x):
            dp =[0 for _ in range(n)]

            f=True
            for j in range(m):
                # print(bin(i)[2:],j)
                if i&(1<<j) :
                    dp[requests[j][0]]-=1
                    dp[requests[j][1]]+=1
            # print(dp)
            for k in range(n):
                if dp[k]!=0:
                    f=False
                    break
            if f:
                maxi = max(maxi,i.bit_count())
        return maxi
          
                    
        
        