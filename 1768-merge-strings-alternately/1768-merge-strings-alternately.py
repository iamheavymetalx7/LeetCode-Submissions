class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newstr=""
        i,j=0,0
        while i<len(word1) and j<len(word2):
            newstr+=word1[i]
            i+=1
            newstr+=word2[j]
            j+=1
        
        while i<len(word1):
            newstr+=word1[i]
            i+=1
        while j<len(word2):
            newstr+=word2[j]
            j+=1
            
        return newstr