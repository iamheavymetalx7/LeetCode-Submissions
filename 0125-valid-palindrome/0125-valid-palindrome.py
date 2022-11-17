class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for i in range(len(s)):
            if s[i].isalnum():
                string+=s[i]
                
        string = string.lower()

        
        for i in range(int((len(string)+1)/2)):
            if string[i]!=string[len(string)-i-1]:
                return False
        return True
                