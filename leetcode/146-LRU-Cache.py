class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.kv = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.kv: 
            node = self.kv[key]
            self._remove(node)
            self._add(node)
            return self.kv[key].value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            self._remove(self.kv[key])
        node = Node(key, value)
        self._add(node)
        self.kv[key] = node
        if len(self.kv) > self.capacity:
            lruNode = self.head.next
            self._remove(lruNode)
            del self.kv[lruNode.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node
