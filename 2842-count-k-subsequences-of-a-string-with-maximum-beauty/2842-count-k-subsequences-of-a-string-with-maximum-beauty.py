class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        cnter = Counter(s)
        
        vals = sorted([v for v in cnter.values()],reverse=True)
        
        max_sum = sum(vals[:k])
        MOD = int(1e9)+7
        n=len(vals)
        
        
        @cache
        def recur(i,k,cur_sum):
            if k==0:
                if cur_sum == max_sum:
                    return 1
                return 0
            
            if i>=n:
                return 0
            
            ans =0
            
            ans = (ans+(vals[i]*recur(i+1,k-1,cur_sum+vals[i]))%MOD)%MOD
            ans = (ans+recur(i+1,k,cur_sum))%MOD
            
            return ans
        
        val = recur(0,k,0)
        return val