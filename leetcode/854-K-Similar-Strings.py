class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def getNeighbors(s1, s2):
            i = 0
            while i < len(s1):
                if s1[i] != s2[i]:
                    break
                i += 1
            res = []
            for j in range(i + 1, len(s1)):
                if s1[j] == s2[i]:
                    s1Arr = list(s1)
                    s1Arr[i], s1Arr[j] = s1Arr[j], s1Arr[i]
                    res.append("".join(s1Arr))
            return res
        queue = deque()
        queue.append(s1)
        level, visited = 0, set()
        while queue:
            size = len(queue)
            for _ in range(size):
                tmp = queue.popleft()
                if tmp == s2: return level
                neighbors = getNeighbors(tmp, s2)
                for neighbor in neighbors:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            level += 1
