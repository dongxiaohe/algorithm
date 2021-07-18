class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        pre = {i : set() for i in range(1, n + 1)}
        nxt = defaultdict(set)
        for x, y in relations:
            pre[y].add(x)
            nxt[x].add(y)
        queue = deque()
        for course in pre:
            if len(pre[course]) == 0:
                queue.append(course)
        remaining = n - len(queue)
        semesters = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for course in nxt[cur]:
                    pre[course].remove(cur)
                    if len(pre[course]) == 0:
                        queue.append(course)
            semesters += 1
            remaining -= len(queue)
        return semesters if remaining == 0 else -1
