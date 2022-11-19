'''
My approach:

from collections import defaultdict,Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic=defaultdict(set)
        
        c=Counter(s)
        d=Counter(t)
        if len(s)!=len(t) or len(c)!=len(d):
            return False
        
        for i in range(len(s)):
            dic[s[i]].add(t[i])
        
        

        for i,j in dic.items():
            if len(list(j))>1:
                return False
        
        return True
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        vis=set()
        dic={}

        
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in vis:
                    return False
                dic[s[i]]=t[i]
                vis.add(t[i])
        return True
        
        