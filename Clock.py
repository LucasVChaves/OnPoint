from datetime import datetime

class Clock():
    def __init__(self):
        self.entranceTime = datetime()
        self.exitTime = datetime()

    # OBS: Precisa implementar

    # Getters

    def getEntranceTime(self):
        return self.entranceTime
    
    def getExitTime(self):
        return self.exitTime
    
    # Setters
    
    def setEntranceTime(self, entranceTime):
        self.entranceTime = entranceTime

    def setExitTime(self, exitTime):
        self.exitTime = exitTime

    def validateClock(self):
        pass

    def actionClockIn(self):
        pass

    def actionClockOut(self):
        pass

    def justifiedDelay(self):
        pass
