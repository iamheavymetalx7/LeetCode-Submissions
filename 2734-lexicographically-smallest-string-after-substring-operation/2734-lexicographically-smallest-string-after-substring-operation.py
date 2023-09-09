class Solution:
    def smallestString(self, s: str) -> str:
        n=len(s)
        i=0
        
        if s=="a"*(n):
            return "a"*(n-1)+"z"
        
        
        while i<n and s[i]=="a":
            i+=1
            
            
        
        f=False
        for j in range(i,n):
            if s[j]=="a":
                f=True
                break
                
        if not f:
            j=n
        def change(x):
            cur =""
            for i in range(len(x)):
                t = ord(x[i])
                t-=1
                cur+=chr(t)
            return cur
                
        
        string = s[:i]+change(s[i:j])+s[j:]
        
        return string