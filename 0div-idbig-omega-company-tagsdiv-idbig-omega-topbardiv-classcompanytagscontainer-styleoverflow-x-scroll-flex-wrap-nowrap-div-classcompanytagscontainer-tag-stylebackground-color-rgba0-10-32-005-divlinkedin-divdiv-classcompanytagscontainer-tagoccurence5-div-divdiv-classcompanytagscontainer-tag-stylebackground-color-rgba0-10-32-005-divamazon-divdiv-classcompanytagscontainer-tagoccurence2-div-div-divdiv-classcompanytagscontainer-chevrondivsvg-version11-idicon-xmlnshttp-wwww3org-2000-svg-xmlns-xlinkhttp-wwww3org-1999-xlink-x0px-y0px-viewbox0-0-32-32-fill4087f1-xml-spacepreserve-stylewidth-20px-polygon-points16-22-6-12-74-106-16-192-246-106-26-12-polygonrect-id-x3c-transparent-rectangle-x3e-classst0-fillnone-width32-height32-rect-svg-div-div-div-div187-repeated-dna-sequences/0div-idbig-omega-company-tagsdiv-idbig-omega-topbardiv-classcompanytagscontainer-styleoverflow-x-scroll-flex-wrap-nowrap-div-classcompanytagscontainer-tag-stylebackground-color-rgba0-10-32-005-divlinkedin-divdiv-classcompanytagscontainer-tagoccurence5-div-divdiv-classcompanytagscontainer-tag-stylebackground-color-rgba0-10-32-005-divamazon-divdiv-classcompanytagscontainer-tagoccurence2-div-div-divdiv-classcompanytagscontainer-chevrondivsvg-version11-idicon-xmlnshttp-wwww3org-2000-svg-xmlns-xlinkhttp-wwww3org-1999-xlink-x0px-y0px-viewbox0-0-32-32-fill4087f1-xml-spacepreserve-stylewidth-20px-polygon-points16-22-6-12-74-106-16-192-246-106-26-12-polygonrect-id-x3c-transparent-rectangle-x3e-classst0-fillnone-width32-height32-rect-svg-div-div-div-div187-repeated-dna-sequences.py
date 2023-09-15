class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)    
        
        dic=defaultdict(int)
        arr=[]
        
        for i in range(n-10+1):
            if s[i:i+10] in dic and dic[s[i:i+10]]==1:
                arr.append(s[i:i+10])
            dic[s[i:i+10]]+=1
        
        return arr