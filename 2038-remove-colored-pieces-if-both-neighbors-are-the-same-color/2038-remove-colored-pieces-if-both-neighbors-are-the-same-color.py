class Solution:
    def winnerOfGame(self, clrs: str) -> bool:
        n = len(clrs)
        
        cntA,cntB = 0,0
        
        
        
        for i in range(1,n-1):
            # print(clrs[i-1],clrs[i],clrs[i+1])
            if clrs[i-1]==clrs[i]==clrs[i+1]=="A":
                cntA+=1
            elif clrs[i-1]==clrs[i]==clrs[i+1]=="B":
                cntB+=1
                
        # print(cntA,cntB)
                
        if cntA ==0:
            return False
        
        if cntA>cntB:
            return True
        return False
        
                