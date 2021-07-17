class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        pre = {i: set() for i in range(1, n + 1)}
        nxt = defaultdict(set)
        for x, y in relations:
            pre[y].add(x)
            nxt[x].add(y)
        queue = [x for x in pre if not pre[x]]
        remaining = n - len(queue)
        ans = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                for course in nxt[cur]:
                    pre[course].remove(cur)
                    if not pre[course]:
                        queue.append(course)
            ans += 1
            remaining -= len(queue)
        return ans if remaining == 0 else -1

