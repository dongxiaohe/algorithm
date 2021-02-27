class Node:
    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq
class LFUCache:

    def __init__(self, capacity: int):
        self.kv = {}
        self.freq = defaultdict(OrderedDict)
        self.capacity = capacity
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key in self.kv:
            node = self.kv[key]
            self.freq[node.freq].move_to_end(node)
            self.freq[node.freq].popitem()
            node.freq += 1
            self.freq[node.freq][node] = None # Use OrderDict as LRU (Double Linked List)
            if len(self.freq[self.minFreq]) == 0:
                self.minFreq += 1
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.kv:
            node = self.kv[key]
            self.freq[node.freq].move_to_end(node)
            self.freq[node.freq].popitem()
            node.val = value
            node.freq += 1
            self.freq[node.freq][node] = None
            if len(self.freq[self.minFreq]) == 0:
                self.minFreq += 1
        else:
            if len(self.kv) == self.capacity:
                evictedNode = self.freq[self.minFreq].popitem(last = False)[0]
                del self.kv[evictedNode.key]
            self.minFreq = 1
            node = Node(key, value, 1)
            self.freq[1][node] = None
            self.kv[key] = node

