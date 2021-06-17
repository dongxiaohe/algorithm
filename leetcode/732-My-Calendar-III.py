class MyCalendarThree:

    def __init__(self):
        self.bookings = defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.bookings[start] += 1
        self.bookings[end] -= 1
        _max, ongoing = 0, 0
        for key in sorted(self.bookings.keys()):
            meetingsCnt = self.bookings[key]
            ongoing += meetingsCnt
            _max = max(_max, ongoing)
        return _max

