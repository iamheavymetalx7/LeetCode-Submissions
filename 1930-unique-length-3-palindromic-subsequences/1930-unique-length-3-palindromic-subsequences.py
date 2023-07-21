class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        left=set()
        right = Counter(s)
        n=len(s)
        res = set()
        
        for i in range(n):  ## treating s[i] as middle character
            
            right[s[i]]-=1
            if right[s[i]]==0:
                del right[s[i]]
            
            for j in range(26):
                c = chr(ord('a')+j)
                
                if c in left and c in right:
                    res.add((s[i],c))
            left.add(s[i])
        
        return len(res)
        
