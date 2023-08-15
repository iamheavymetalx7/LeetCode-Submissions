class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        
        n=len(nums)
        diff=defaultdict(int)
        ssum = defaultdict(int)
        
        for i in range(n//2):
            a,b= nums[i],nums[-i-1]
            
            mmin = min(a,b)+1
            mmax = max(a,b)+limit
            
            diff[mmin]-=1
            diff[mmax+1]+=1
            
            ssum[a+b]+=1
        
        
        cur=n
        ans=int(1e18)
        for i in range(2,max(ssum)+1):
            cur+=diff[i]
            ans= min(ans,cur-ssum[i])
        return ans
            