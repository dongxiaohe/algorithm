class MyCalendar:
    def __init__(self):
        self.timeslot = []

    def book(self, start: int, end: int) -> bool:
        index = bisect_right(self.timeslot, [start, end])
        _end, _start = float("-inf"), float("inf")
        if index < len(self.timeslot):
            _start = self.timeslot[index][0]
        if index - 1 >= 0:
            _end = self.timeslot[index - 1][1]
        if start >= _end and end <= _start:
            insort(self.timeslot, [start, end])
            return True
        return False
