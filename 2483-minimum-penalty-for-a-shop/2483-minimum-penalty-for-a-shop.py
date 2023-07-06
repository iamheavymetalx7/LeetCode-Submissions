class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        
        prefixY =[0]*(n)
        prefixN=[0]*(n)
        
        prefixY[0]=1 if customers[0]=="Y" else 0
        prefixN[0]=1 if customers[0]=="N" else 0
        
        
        for i in range(1,n):
            if customers[i]=="Y":
                prefixY[i]=1+prefixY[i-1]
            else:
                prefixY[i]=prefixY[i-1]
                
            if customers[i]=="N":
                prefixN[i]=1+prefixN[i-1]
            else:
                prefixN[i]=prefixN[i-1]
        
        print(prefixY, prefixN)
        minPenalty = 10**9
        to_ret=-1
        for i in range(n):
            ans=0
            if customers[i]=="N":
                if i==0:
                    ans+=0
                    ans+=prefixY[-1]-prefixY[i]
                    print(i,ans)
                elif i==n-1:
                    ans=0
                    ans+=prefixN[i-1]
                    print(i,ans)
                else:
                    ans+=prefixY[-1]-prefixY[i]
                    ans+=prefixN[i-1]
                    print(i,ans)
                if minPenalty>ans:
                    minPenalty = ans
                    to_ret=i
        
        
        ## if i close after the end
        if minPenalty>prefixN[-1]:
            to_ret=n
            
            
        
        if to_ret==-1:
            return(n)
        return to_ret
                    