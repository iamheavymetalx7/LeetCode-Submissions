'''
If the ending index of substring is i,
the starting position should be on the left of min(last),
in order to have all 3 different letters.
And in this case, the starting index can be in range [0, min(last)],
min(last) + 1 in total.

https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/516977/JavaC%2B%2BPython-Easy-and-Concise

'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res=0
        last =[-1]*(3)
        
        for i,c in enumerate(s):
            last[ord(s[i])-ord('a')]=i
            
            res+=1+min(last)
        return res