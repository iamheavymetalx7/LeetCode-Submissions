class Solution:

    def isPal(self,s,start,end):
        while start<=end:
            if s[start]!=s[end]:
                return False
            start,end=start+1,end-1
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        
        ans=[]
        n=len(s)
        
        def recur(index,s,path):
            if index>=len(s):
                ans.append(path)
                return
            
            for i in range(index,len(s)):
                if self.isPal(s,index,i):
                    recur(i+1,s,path+[s[index:i+1]])
            
        recur(0,s,[])
        
        return ans
    
        