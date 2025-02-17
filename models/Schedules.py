from datetime import datetime

class Schedules:
    def __init__(self, timeIn, hourlyLoad, lunchTime, initialVacation, finishVacation):
        self.timeIn: datetime = timeIn
        self.hourlyLoad: datetime = hourlyLoad
        self.lunchTime: datetime = lunchTime
        self.initialVacation: datetime = initialVacation
        self.finishVacation: datetime = finishVacation
