'''
discussion:
1. https://www.geeksforgeeks.org/construct-the-largest-number-whose-sum-of-cost-of-digits-is-k/
2. https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/discuss/654490/DP-is-Easy!-5-Step-DP-THINKING-process-EXPLAINED!
3. topics: unbounded knapsack dp, optimization
4. came across this qn from VG_YT_DE_SHAW
'''
import sys
sys.set_int_max_str_digits(10**8)
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        
        n=len(cost)
        
        def getBigger(s,t):
            if '0' in s:
                return t
            if '0' in t:
                return s
            if int(s)>int(t):
                return s
            return t
        
        @cache
        def recur(idx,remain):
            if remain==0:
                return ""
            if idx==n or remain<0:
                return "0"
            
            take = str(idx+1)+recur(0,remain-cost[idx])
            nottake = recur(idx+1,remain)
            
            return getBigger(take,nottake)
        
        val =recur(0,target)
        return '0' if val.count('0')>0 else val
        
        
            
            
            