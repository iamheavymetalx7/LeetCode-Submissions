class Solution:
    def bestClosingTime(self, c: str) -> int:
        s=len(c)

        y=[]
        n=[]
        y.append(0)
        n.append(0)
        
        cnt=0
        for i in range(s):
            if c[i]=="N":
                cnt+=1
            n.append(cnt)
                
        cnt=0
        for i in range(s-1,-1,-1):
            if c[i]=="Y":
                cnt+=1
            y.append(cnt)
                
        y = y[::-1]
        
        
        ans=10**9
        idx=0
        
        for i in range(s+1):
            curr = y[i]+n[i]
            if curr<ans:
                ans=curr
                idx=i
        return idx
            