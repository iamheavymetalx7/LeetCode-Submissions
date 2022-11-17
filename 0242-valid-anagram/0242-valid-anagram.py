'''
approach 1: ##my solution
class Solution:
    def isAnagram(self, s, t):
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2
        

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=''.join(sorted(s))
        t=''.join(sorted(t))
        if s==t:
            return True
        return False        
    
## sorted(s)=['a', 'a', 'a', 'g', 'm', 'n', 'r']
## s= "anagram"
## t= "nagaram"