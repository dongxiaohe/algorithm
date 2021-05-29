class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.incr = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.incr.append(0)

    def pop(self) -> int:
        if not self.stack: return -1
        if len(self.stack) > 1:
            self.incr[-2] += self.incr[-1]
        return self.stack.pop() + self.incr.pop()

    def increment(self, k: int, val: int) -> None:
        if self.incr:
            k = min(k, len(self.incr)) - 1
            self.incr[k] += val

