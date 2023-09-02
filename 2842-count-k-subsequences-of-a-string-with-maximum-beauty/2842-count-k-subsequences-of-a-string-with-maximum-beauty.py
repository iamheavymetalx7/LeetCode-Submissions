class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        cnter = Counter(s)
        
        print(len(s))
        print(cnter)
        
        vals = sorted([v for v in cnter.values()],reverse=True)
        
        max_sum = sum(vals[:k])
        MOD = int(1e9)+7
        n=len(vals)
        
        
        

        # dp =[[[-1 for _ in range(max_sum+5)]for _ in range(k+5)] for _ in range(n+5)]
        # @cache
        
        dp = {}
        def recur(i,k,cur_sum):

            if k==0:
                if cur_sum == max_sum:
                    return 1
                return 0
            
            if i>=n:
                return 0
            
            if str(i)+"$"+str(k)+"$"+str(cur_sum) in dp:
                return dp[str(i)+"$"+str(k)+"$"+str(cur_sum) ]
            
            
            ans =0
            
            ans = (ans+(vals[i]*recur(i+1,k-1,cur_sum+vals[i]))%MOD)%MOD
            ans = (ans+recur(i+1,k,cur_sum))%MOD
            
            dp[str(i)+"$"+str(k)+"$"+str(cur_sum) ] = ans
            return dp[str(i)+"$"+str(k)+"$"+str(cur_sum) ]
            # dp[i][k][cur_sum]=ans
            # return dp[i][k][cur_sum]
            # return ans
        val = recur(0,k,0)
        return val