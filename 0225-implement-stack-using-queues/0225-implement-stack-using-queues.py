class MyStack:

    def __init__(self):
        self.q1=deque()
        self.q2=deque()
        
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        while len(self.q1)>1:
            ele = self.q1.popleft()
            self.q2.append(ele)
        
        val =  self.q1.popleft()
        self.q1,self.q2 = self.q2,self.q1
        return val
    
        
        

    def top(self) -> int:
        while len(self.q1)>1:
            ele = self.q1.popleft()
            self.q2.append(ele)
        
        val =  self.q1.popleft()
        self.q2.append(val)
        self.q1,self.q2 = self.q2,self.q1
        return val
        

    def empty(self) -> bool:
        if len(self.q1)==0 and not len(self.q2):
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()