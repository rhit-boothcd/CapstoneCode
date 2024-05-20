import statistics


class horseStats:
    def __init__(self, timeData, forceData) -> None:
        self.forceData = forceData
        self.timeData = timeData
        self.data = [[0] * 8 for _ in range(8)]
        self.averageRead()
        self.minimum()
        self.maximum()
        self.range()
        self.flux()
        self.stddev()
        #return self.data
        
    def averageRead(self):
        for i in range(8):
            self.data[i][0] = statistics.mean(self.forceData[i][int(self.timeData[0]):int(self.timeData[1])])

    def stddev(self):
        for i in range(8):
            self.data[i][7] = statistics.stdev(self.forceData[i][int(self.timeData[0]):int(self.timeData[1])])

    def range(self):
        for i in range(8):
            if self.data[i][0] != 0:
                self.data[i][1] = (self.data[i][3]-self.data[i][2])

    def flux(self):
        pass

    def maximum(self):
        for i in range(8):
            self.data[i][3] = max(self.forceData[i][int(self.timeData[0]):int(self.timeData[1])])
            self.data[i][5] = (self.forceData[i][int(self.timeData[0]):int(self.timeData[1])]).index(self.data[i][3])
            self.data[i][5] = int(self.data[i][5]*(5/6) + int(self.timeData[0])) + 4


    def minimum(self):
        for i in range(8):
            self.data[i][2] = min(self.forceData[i][int(self.timeData[0]):int(self.timeData[1])])
            self.data[i][4] = (self.forceData[i][int(self.timeData[0]):int(self.timeData[1])]).index(self.data[i][2])
            self.data[i][4] = int(self.data[i][4]*(5/6)  + int(self.timeData[0])) + 4

    def tilt(self):
        pass
