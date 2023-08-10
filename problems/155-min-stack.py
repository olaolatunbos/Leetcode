class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        top = self.stack.pop()
        self.stack.append(top)
        return top

        

    def getMin(self) -> int:
        return self.minStack[-1]
        
    

obj = MinStack()
obj.push(10)
obj.push(20)
obj.pop()
param_3 = obj.top()
param_4= obj.getMin()
print(param_3)
print(param_4)