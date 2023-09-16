class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        
        
        def helper(inp):
            s=list(inp)
            n=len(inp)
            
            cnt,i=0,0
            
            while i<n//2:
                left = i
                right= n-left-1
                
                while left<right:
                    if s[left]==s[right]:
                        break
                    else:
                        right-=1
                
                if left==right:
                    # s[left] is the character in the middle of the palindrome
                    s[left],s[left+1]=s[left+1],s[left]
                    cnt+=1
                else:
                    for j in range(right,n-left-1):
                        s[j],s[j+1]=s[j+1],s[j]
                        cnt+=1
                    i+=1
            return cnt
        
        return min(helper(s),helper(s[::-1]))