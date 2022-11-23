'''
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        l,i=0,0
        cnt=0
        
        while i<len(g) and l<len(s):
            if s[l]>=g[i]:
                i+=1
                l+=1
                cnt+=1
            else:
                i+=1
        return cnt
'''
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        l,i=0,0
        
        while i<len(g) and l<len(s):
            if s[l]>=g[i]:
                i+=1
                l+=1
            else:
                i+=1
        return l