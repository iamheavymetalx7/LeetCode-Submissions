class Solution:
    def robotWithString(self, s: str) -> str:
        ans,t=[],[]
        dic = Counter(s)
        
        for char in s:
            t.append(char)

            if dic[char]==1:
                del dic[char]
            else:
                dic[char]-=1
            while t and dic and min(dic)>=t[-1]:
                ans.append(t[-1])
                t.pop()
        ans+=t[::-1]
        
        return ''.join(ans)
        