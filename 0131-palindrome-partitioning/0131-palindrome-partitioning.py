class Solution:
    
    def recur(self,path,res,index,s):
        if index==len(s):
            res.append(path.copy())
            return
        
        for i in range(index,len(s)):
            if self.isPal(s,index,i):
                path.append(s[index:i+1])
                self.recur(path,res,i+1,s)
                path.pop()
    
    
    def partition(self, s: str) -> List[List[str]]:
        path=[]
        res=[]
        self.recur(path,res,0,s)
        return res
    
   


    def isPal(self,s,start,end):
        
        while start<=end:
            if s[start]!=s[end]:
                return False
            start,end=start+1,end-1
        return True
        