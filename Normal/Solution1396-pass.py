# 1396、设计地铁系统


class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.routes = {}

    def checkIn(self, id_: int, stationName: str, t: int) -> None:
        self.customers[id_] = [stationName, t]

    def checkOut(self, id_: int, stationName: str, t: int) -> None:
        route = self.customers[id_][0] + ' ' + stationName
        time_ = t - self.customers[id_][1]
        if route in self.routes:
            self.routes[route][0] += time_
            self.routes[route][1] += 1
        else:
            self.routes[route] = [time_, 1]
        self.customers.pop(id_)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = self.routes[startStation + ' ' + endStation]
        return route[0] / route[1]
