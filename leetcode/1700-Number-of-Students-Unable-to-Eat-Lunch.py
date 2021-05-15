class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentsKv, sandwichesKv = collections.Counter(students), collections.Counter(sandwiches)
        if studentsKv == sandwichesKv: return 0
        while students:
            if studentsKv[sandwiches[0]] == 0: return len(students)
            head = students.pop(0)
            if head == sandwiches[0]:
                sandwiches.pop(0)
                studentsKv[head] -= 1
            else:
                students.append(head)
        return 0
