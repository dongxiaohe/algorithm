class RandomizedCollection:

    def __init__(self):
        self.kv = collections.defaultdict(set)
        self.arr = []
        
    def insert(self, val: int) -> bool:
        self.kv[val].add(len(self.arr))
        self.arr.append(val)
        return len(self.kv[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.kv or len(self.kv[val]) == 0:
            return False
        idx = self.kv[val].pop()
        if idx == len(self.arr) - 1:
            self.arr.pop() 
        else:
            val = self.arr[len(self.arr) - 1]
            self.kv[val].remove(len(self.arr) - 1)
            self.kv[val].add(idx)
            self.arr[idx], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[idx]
            self.arr.pop() 
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
