class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(id, employees):
            return employees[id].importance + sum([dfs(_id, employees) for _id in employees[id].subordinates])
        employeesDict = {}
        for employee in employees:
            employeesDict[employee.id] = employee
        return dfs(id, employeesDict)

