class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n,m=len(text1),len(text2)
        
        dp=[[-1]*m for _ in range(n)]
        def f(i1,i2):
            if i1==0 or i2==0:
                if i1==0:
                    for jj in range(i2,-1,-1):
                        if text1[0]==text2[jj]:
                            return 1
                    else:
                        return 0
                
                if i2==0:
                    for jj in range(i1,-1,-1):
                        if text1[jj]==text2[0]:
                            return 1
                    else:
                        return 0
            # print(i1,i2)
                            
            
            if dp[i1][i2]!=-1:
                return dp[i1][i2]
            
            if text1[i1]==text2[i2]:
                dp[i1][i2]=1+f(i1-1,i2-1)
            else:

                one = f(i1-1,i2)
                two = f(i1,i2-1)
                dp[i1][i2] =max(one, two)
            
            return dp[i1][i2]

        return f(n-1,m-1)
        
        
            