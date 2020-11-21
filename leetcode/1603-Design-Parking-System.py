class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.spaces = collections.defaultdict(int)
        self.spaces[1] = big
        self.spaces[2] = medium
        self.spaces[3] = small

    def addCar(self, carType):
        if self.spaces[carType] >= 1:
            self.spaces[carType] -= 1
            return True
        return False
