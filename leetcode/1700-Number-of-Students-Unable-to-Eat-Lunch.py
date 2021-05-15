class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = collections.Counter(students)
        k = 0 
        while k < len(sandwiches):
            if cnt[sandwiches[k]] > 0:
                cnt[sandwiches[k]] -= 1
            else:
                break
            k += 1
        return len(sandwiches) - k
