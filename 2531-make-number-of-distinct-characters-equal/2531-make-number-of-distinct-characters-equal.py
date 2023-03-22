from collections import Counter
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        
        cnter1=Counter(word1)
        cnter2=Counter(word2)
        
        set1=set(list(cnter1.keys()))
        set2=set(list(cnter2.keys())) 
        
        for k1 in cnter1:
            for k2 in cnter2:
                s1_copy=set1.copy()
                s2_copy=set2.copy()
                
                if cnter1[k1]==1:
                    s1_copy.discard(k1)
                s1_copy.add(k2)
                
                if cnter2[k2]==1:
                    s2_copy.discard(k2)
                s2_copy.add(k1)
                
                if len(s1_copy)==len(s2_copy):
                    return True
        return False