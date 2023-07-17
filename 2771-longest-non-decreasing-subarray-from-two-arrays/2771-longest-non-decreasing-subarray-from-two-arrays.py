'''

It depends from which array we are taking, so we keep a track of from where we last took!
And after that, we also take a case where we don't take anything till now and build from scratch
'''

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        dp=[[-1]*3 for _ in range(n)]
        def recur(idx,last):
            if idx>=n:
                return 0
            
            if dp[idx][last]!=-1:
                return dp[idx][last]
        
            ans =0
            if last ==0:
                ans=max(ans,1+recur(idx+1,1))
                ans=max(ans,1+recur(idx+1,2))
                ans=max(ans,recur(idx+1,0))
            else:
                
                val=0
                if last==1:
                    val = nums1[idx-1]
                else:
                    val=nums2[idx-1]
                
                if val<=nums1[idx]:
                    ans=max(ans,1+recur(idx+1,1))
                
                if val<=nums2[idx]:
                    ans=max(ans,1+recur(idx+1,2))
            dp[idx][last]=ans
            return dp[idx][last]
                    
                
            
            return dp[idx][alst]
        ans =recur(0,0)
        # print(dp)
        return ans
            