class FrontMiddleBackQueue:
    def __init__(self):
        self.A = deque()
        self.B = deque()
        
    def pushFront(self, val: int) -> None:
        self.A.appendleft(val)
        self.balance()
        
    def pushMiddle(self, val: int) -> None:
        if len(self.A) > len(self.B):
            self.B.appendleft(self.A.pop())
        self.A.append(val)

    def pushBack(self, val: int) -> None:
        self.B.append(val)
        self.balance()
        
    def popFront(self) -> int:
        val = self.A.popleft() if self.A else -1
        self.balance()
        return val

    def popMiddle(self) -> int:
        if not self.A: return -1
        val = self.A.pop()
        self.balance()
        return val
        
    def popBack(self) -> int:
        if not self.B and not self.A: return -1
        val = (self.B or self.A).pop()
        self.balance()
        return val
        
    def balance(self):
        if len(self.A) > len(self.B) + 1:
            self.B.appendleft(self.A.pop())
        elif len(self.A) < len(self.B):
            self.A.append(self.B.popleft())
