class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        string_a = s[:n//2]
        string_b= s[n//2::]
        
        print(string_a)
        print(string_b)
        
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        cnt_a,cnt_b =0,0
        for i in range(n//2):
            if string_a[i] in vowels:
                cnt_a+=1
            if string_b[i] in vowels:
                cnt_b+=1
        return cnt_a==cnt_b