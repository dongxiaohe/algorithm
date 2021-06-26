class Logger:
    def __init__(self):
        self.kv = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.kv and timestamp < self.kv[message] + 10:
            return False
        self.kv[message] = timestamp
        return True
