class MyCalendarTwo:

    def __init__(self):
        self.meetings = []
        self.overlapps = []

    def book(self, start: int, end: int) -> bool:
        for a, b in self.overlapps:
            if b > start and end > a: return False
        for a, b in self.meetings:
            if b > start and end > a:
                self.overlapps.append([max(a, start), min(b, end)])
        self.meetings.append([start, end])
        return True

