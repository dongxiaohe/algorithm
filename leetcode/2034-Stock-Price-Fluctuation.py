class StockPrice(object):

    def __init__(self):
        self.minPrices = []
        self.maxPrices = []
        self.prices = {}
        self.curTime = None
        

    def update(self, timestamp, price):
        heapq.heappush(self.minPrices, [price, timestamp])
        heapq.heappush(self.maxPrices, [-price, timestamp])
        self.prices[timestamp] = price
        if self.curTime is None:
            self.curTime = timestamp
        elif self.curTime < timestamp:
            self.curTime = timestamp

    def current(self):
        return self.prices[self.curTime]
        

    def maximum(self):
        price, timestamp = self.maxPrices[0]
        while -price != self.prices[timestamp]:
            heapq.heappop(self.maxPrices)
            price, timestamp = self.maxPrices[0]
        return -price
        

    def minimum(self):
        price, timestamp = self.minPrices[0]
        while price != self.prices[timestamp]:
            heapq.heappop(self.minPrices)
            price, timestamp = self.minPrices[0]
        return price

