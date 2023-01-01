from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_pattern = list(pattern)
        list_s = s.split(" ")
        # print(list_pattern)
        # print(list_s)
        dic=defaultdict(str)
        dic2=defaultdict(str)
        
        if len(list_pattern)!=len(list_s):
            return False
        for x,y in zip(list_pattern,list_s):
            # print(x,y)
            if x in dic:
                if dic[x]!=y:
                    return False
            else:
                dic[x]=y
                
            if y in dic2:
                if dic2[y]!=x:
                    return False
            else:
                dic2[y]=x
        
        return True