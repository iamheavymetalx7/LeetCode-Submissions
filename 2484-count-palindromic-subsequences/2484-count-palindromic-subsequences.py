class Solution:
    def countPalindromes(self, s: str) -> int:
        
        n=len(s)
        
        
        mod = int(1e9)+7
        
        if n<5:
            return 0
        if n==5:
            if s==s[::-1]:
                return 1
            return 0
        
        @cache
        def dfs(idx,first,second,i):
            
            if i==5:
                return 1
            if idx==n:
                return 0
            

            ## not choosing
            res = dfs(idx+1,first,second,i)
            
            # choosing
            
            if i==0:    ## first digit
                res += dfs(idx+1,int(s[idx]),second,i+1)
                res %= mod
            elif i==1:  ## second digit
                res += dfs(idx+1,first,int(s[idx]),i+1)
                res %= mod
            elif i==2: # third digit can be anything 
                res += dfs(idx+1,first,second,i+1)
                res %= mod
            elif i==3:   # 4th digit should be same as second one
                if int(s[idx])==second:
                    res += dfs(idx+1,first, second,i+1)
                    res %= mod
            elif i==4:  # 5th digit should be same as second one
                if int(s[idx])==first:
                    res += dfs(idx+1, first ,second, i+1)
                    res %= mod
            
            return res
        ans = dfs(0,10,10,0)
        return ans
                