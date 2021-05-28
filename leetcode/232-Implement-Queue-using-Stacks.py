class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []
        
    def push(self, x: int) -> None:
        self.inStack.append(x)
        
    def pop(self) -> int:
        self.peek()
        if not self.outStack: return -1
        return self.outStack.pop()

    def peek(self) -> int:
        if self.outStack:
            return self.outStack[-1]
        while self.inStack:
            self.outStack.append(self.inStack.pop())
        return self.outStack[-1] if self.outStack else -1

    def empty(self) -> bool:
        return not self.inStack and not self.outStack
