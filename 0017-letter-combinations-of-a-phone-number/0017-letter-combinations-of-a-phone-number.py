class Solution:
    def letterCombinations(self, dig: str) -> List[str]:
        
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        ans =[]
        
        n = len(dig)
        
        if not dig:
            return []
        
        def recur(i,s):
            if i==n:
                ans.append(deepcopy(s))
                return
            
            for x in dic[dig[i]]:
                recur(i+1,s+x)
        
        recur(0,"")
        return (ans)
        