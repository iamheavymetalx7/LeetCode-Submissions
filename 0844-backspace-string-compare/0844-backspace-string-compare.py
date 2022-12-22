from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack1,stack2 = deque(),deque()
        
        
        for i in range(len(s)):
            if s[i]!="#":
                stack1.append(s[i])
            else:
                if stack1:
                    stack1.pop()
                else:
                    stack1=deque()
 
                
        for i in range(len(t)):
            if t[i]!="#":
                stack2.append(t[i])
            else:
                if stack2:
                    stack2.pop()
                else:
                    stack2=deque()
        
        print(stack1)
        print(stack2)
        
        return stack1==stack2