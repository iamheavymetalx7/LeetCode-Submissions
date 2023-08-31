class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n =len(receiver)
        
        BITS = 34
        
        dst =[[0]*(n) for _ in range(BITS)]
        sum_ = [[0]*(n) for _ in range(BITS)]
        
        for j in range(n):
            dst[0][j] = receiver[j]
            sum_[0][j] = j+receiver[j]
        
        for i in range(1,BITS):
            for j in range(n):
                dst[i][j] = dst[i-1][dst[i-1][j]]
                sum_[i][j] = sum_[i-1][dst[i-1][j]]+sum_[i-1][j] - dst[i-1][j]
                
        final_dst=[0 for _ in range(n)]
        final_sum =[0 for _ in range(n)]
        
        for j in range(n):
            final_dst[j]=j
            final_sum[j]=j
                
        for i in range(BITS-1,-1,-1):
            if (1<<i)&(k)==0:
                continue
            for j in range(n):
                final_sum[j] = sum_[i][final_dst[j]] +final_sum[j]- final_dst[j]
                final_dst[j] = dst[i][final_dst[j]]
        
        ans =0
        
        for x in final_sum:
            ans=max(ans,x)
        return ans
            
        