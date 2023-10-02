class Solution:
    def winnerOfGame(self, c: str) -> bool:
        cntA,cntB =0,0
        n = len(c)
        for i in range(n):
            if i>=1 and i<=n-2:
                # print(i,c[i-1],c[i],c)
                if c[i]=="A" and c[i-1]==c[i]==c[i+1]:
                    cntA+=1
                elif c[i]=="B" and c[i-1]==c[i]==c[i+1]:
                    cntB+=1
        
        return cntA>cntB