class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        lenS=len(s)
        lenT=len(t)
        ans=0
        
        for i in range(lenS):
            for j in range(lenT):
                
                Si,Tj,d=i,j,0
                
                while Si<lenS and Tj<lenT:
                    if s[Si]!=t[Tj]:
                        d+=1
                    
                    if d==1:
                        ans+=1
                        
                    if d==2: break
                        
                    Si+=1; Tj+=1
                    
        return ans