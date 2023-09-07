class MinStack:

    def __init__(self):
        self.answer = []

    def push(self, val: int) -> None:
        currmin = self.getMin()
        
        if currmin == None or val < currmin : 
            currmin = val
        self.answer.append((val,currmin))

    def pop(self) -> None:
        self.answer.pop()

    def top(self) -> int:
        if len(self.answer) == 0 :
            return None
        return self.answer[-1][0]

    def getMin(self) -> int:
        if len(self.answer) == 0 :
            return None
        return self.answer[len(self.answer)-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()