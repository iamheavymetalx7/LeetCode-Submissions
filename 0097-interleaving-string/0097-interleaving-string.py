class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        

        
        n,m,k = len(s1),len(s2),len(s3)
        
        if n+m!=k:
            return False     
        
        @cache
        def recur(i,j):
            if i==len(s1):
                return s2[j:]==s3[i+j:]
            
            if j==len(s2):
                return s1[i:]==s3[i+j:]
            
            
            choose1,choose2=False,False
            
            if s1[i]==s3[i+j]:
                choose1 = recur(i+1,j)
            if s2[j]==s3[i+j]:
                choose2 =recur(i,j+1)
                
            return choose1 or choose2
        return recur(0,0)