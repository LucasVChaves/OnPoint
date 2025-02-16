from datetime import datetime

class Schedules:
    def __init__(self, timeIn, hourlyLoad, lunchTime, initialVacation, finishVacation):
        self.timeIn = timeIn
        self.hourlyLoad = hourlyLoad
        self.lunchTime = lunchTime
        self.initialVacation = initialVacation
        self.finishVacation = finishVacation

    # Getters

    def getTimeIn(self):
        return self.timeIn
    
    def getHourlyLoad(self):
        return self.hourlyLoad
    
    def getLunchTime(self):
        return self.lunchTime
    
    def getInitialVacation(self):
        return self.initialVacation
    
    def getFinishVacation(self):
        return self.finishVacation
    
    # Setters

    def setTimeIn(self, timeIn):
        self.timeIn = timeIn

    def setHourlyLoad(self, hourlyLoad):
        self.hourlyLoad = hourlyLoad

    def setLunchTime(self, lunchTime):
        self.lunchTime = lunchTime

    def setInitialVacation(self, initialVacation):
        self.initialVacation = initialVacation 
    
    def setFinishVacation(self, finishVacation):
        self.finishVacation = finishVacation
    

