class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        
        def helper(string,opencnt, closecnt):
            if opencnt==n and closecnt==n:
                ans.append(string)
                
            else:
                if opencnt<n:
                    helper(string+"(", opencnt+1, closecnt)
                if closecnt<opencnt:
                    helper(string+")", opencnt, closecnt+1)
        helper("",0,0)
        return ans
            
            
            
            