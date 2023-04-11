class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        
        stack=[]
        
        for c in num:
            while stack and k and stack[-1]>c:
                stack.pop()
                k-=1
            stack.append(c)
        
        while stack and k>0:
            stack.pop()
            k-=1
        
        if not stack:
            return "0"
        return str(int("".join(stack)))
        
        
        