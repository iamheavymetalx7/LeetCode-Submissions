from collections import deque
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack=deque()
        arr=[0]*len(temp)
        
        for i,v in enumerate(temp):
            while stack and stack[-1][1]<v:
                index, val= stack.pop()
                arr[index]=i-index
            stack.append([i,v])
            
        return arr
            
        