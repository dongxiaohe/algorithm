class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited, kv = [False] * 26, defaultdict(int)
        for ch in s:
            kv[ch] += 1
        stack = []
        for ch in s:
            kv[ch] -= 1
            index = ord(ch) - 97
            if visited[index]: continue
            while stack and stack[-1] > ch and kv[stack[-1]] > 0:
                visited[ord(stack.pop()) - 97] = False
            visited[index] = True
            stack.append(ch)
        return "".join(stack)
