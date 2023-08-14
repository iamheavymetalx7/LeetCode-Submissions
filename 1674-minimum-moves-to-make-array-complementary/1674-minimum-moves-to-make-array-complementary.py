'''
1. https://leetcode.com/problems/minimum-moves-to-make-array-complementary/discuss/952800/Python-Simple-O(n%2Bk)-solution
2. https://www.youtube.com/watch?v=uyV0p6zy9DU

3. https://leetcode.com/problems/minimum-moves-to-make-array-complementary/discuss/953393/Detailed-Explain-Why-We-Need-Difference-Array

'''
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        
        diff = defaultdict(int)
        ssum = defaultdict(int)
        
        n=len(nums)
        
        for i in range(n//2):
            a=nums[i]
            b=nums[-i-1]
            
            mmin=min(a,b)+1
            mmax=max(a,b)+limit
            
            diff[mmin]-=1
            diff[mmax+1]+=1
            
            ssum[a+b]+=1
        
        
        ans = int(1e18)
        cur = n
        
        for i in range(2,max(diff)):
            cur+=diff[i]
            ans = min(ans, cur-ssum[i])
        return ans
        
        