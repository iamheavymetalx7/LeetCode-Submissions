class Solution:
## O(N^2) solution, we keep each char of s as centre and then imagine what needs to be done

    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        res=""
        resLen=0
        
        for i in range(n):
            # odd - length
            left,right =i,i
            while left>=0 and right<n and s[left]==s[right]:
                if right-left+1>resLen:
                    res=s[left:right+1]
                    resLen=right-left+1
                right+=1
                left-=1
            
            # even - length
            
            left, right = i,i+1
            while left>=0 and right< n and s[left]==s[right]:
                if right-left+1>resLen:
                    res=s[left:right+1]
                    resLen=right-left+1
                right+=1
                left-=1
        return res
        
        

    
# Brute force : O(N^3) solution
# Shouln't work : 10^9 - TLE
#     def isPalindrome(self, sub_str):
#         n=len(sub_str)
#         for i in range(n//2):
#             if sub_str[i]!=sub_str[n-1-i]:
#                 return False
#         return True
    
#     def longestPalindrome(self, s: str) -> str:
#         to_ret =""
#         ans=0
#         n=len(s)
#         print(n)
#         for i in range(n):
#             for j in range(i,n):
#                 if self.isPalindrome(s[i:j+1]) and (j+1-i)>ans:
#                     ans=(j+1-i)
#                     to_ret = (s[i:j+1])
                    
#         return to_ret