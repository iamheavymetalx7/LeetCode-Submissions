class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=[]
        
        def recur(index,string):
            if index>=len(s):
                ans.append(string)
            else:
                if s[index].isalpha():
                    recur(index+1,string+s[index].swapcase())
                recur(index+1,string+s[index])
        recur(0,"")
        
        return ans