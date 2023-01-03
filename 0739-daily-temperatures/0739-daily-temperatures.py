from collections import deque
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack=deque()
        arr=[]
        n=len(temp)
        
        for i in range(n-1,-1,-1):
            if len(stack)==0:
                arr.append(0)
            else:
                while stack and stack[-1][1]<=temp[i]:
                    stack.pop()
                if len(stack)==0:
                    arr.append(0)
                else:
                    arr.append(stack[-1][0]-i)
            stack.append([i,temp[i]])
        return arr[::-1]