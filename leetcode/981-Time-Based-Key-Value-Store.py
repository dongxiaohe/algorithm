class TimeMap:
    def __init__(self):
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.kv[key]
        l, r = 0, len(arr)
        while l < r:
            m = l + (r - l >> 1)
            if arr[m][0] <= timestamp: l = m + 1
            else: r = m 
        return "" if l == 0 else arr[l - 1][1]
