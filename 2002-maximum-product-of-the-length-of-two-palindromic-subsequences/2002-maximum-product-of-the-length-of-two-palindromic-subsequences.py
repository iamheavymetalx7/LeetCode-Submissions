'''
odd length palindrome -> abcba
even length palindrome -> abba

since length is small it has to be backtracking
so we decide whether we wish to choose an element or not, i.e. we try to create one
subsequence of characters, and find among them the longest palindromic substring
'''
def longestpalSubseq(s):
        t = s[::-1]
        
        n,m=len(s),len(t)
        
        dp=[[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=0
        
        for j in range(m+1):
            dp[0][j]=0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                if s[i-1]==t[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[n][m]

class Solution:
    def maxProduct(self, s: str) -> int:
        ans =0
        def cnt_length_palindrome(m):
            nonlocal ans
            val =0
            string1=""
            string2=""
            for i in range(len(s)):
                if m&(1<<i):
                    string1+=s[i]
                else:
                    string2+=s[i]
            # print(string1, string2)
            if string1 and string2:
                ans = max(ans,longestpalSubseq(string1)*longestpalSubseq(string2))
        mask = 0
        n=len(s)
        cnt=0
        def recur(idx,mask):
            nonlocal cnt
            if idx>=n:
                cnt+=1
                if mask!=0 or mask!=((1<<n)-1):
                    cnt_length_palindrome(mask)
                return mask
            for i in range(idx,n):
                mask ^= (1<<i)
                recur(i+1,mask)
                mask ^= (1<<i)
        

        recur(0,0)
        # print(cnt,"at the end")
        return ans
            