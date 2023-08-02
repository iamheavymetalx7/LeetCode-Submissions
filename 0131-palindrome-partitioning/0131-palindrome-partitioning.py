class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPal(string):
            return string == string[::-1]
        
        n=len(s)
        
        ans =[]
        
        def recur(idx,arr):
            if idx>=n:
                ans.append(arr.copy())
            
            
            for i in range(idx,n):
                if isPal(s[idx:i+1]):
                    recur(i+1,arr+[s[idx:i+1]])
        recur(0,[])
        
        return ans
        