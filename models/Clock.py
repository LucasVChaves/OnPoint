from datetime import datetime
import Schedules


class Clock():
    def __init__(self):
        self.entranceTime: datetime = datetime()
        self.exitTime: datetime = datetime()()
        pass

    def validateStart(self,Schedules: Schedules, work_start: datetime):
        current_time = datetime.now()
        work_start = Schedules.timeIn
        
        if self.entranceTime > work_start:
            raise ValueError("Entrance time is greater than work start")
        if self.entranceTime < work_start:
            raise ValueError("Entrance time is less than work start")
        if self.entranceTime == work_start:
            return True

    def validateEnd(self,Schedules: Schedules,exitTime: datetime):

        current_time = datetime.now()
        work_start = Schedules.timeIn
        work_end = Schedules.timeIn + Schedules.hourlyLoad + Schedules.lunchTime
        overtime = exitTime - work_end

        if self.exitTime > work_end:
            raise ValueError("Exit time is {overtime} hour(s) after than work end")
        if self.exitTime < work_end:
            raise ValueError("Exit time is {overtime} hour(s) before than work end")
        if self.exitTime == work_end:
            return True

    """def validateLunch(self,Schedules: Schedules, lunchTime: datetime):
        work_start = Schedules.timeIn
        work_end = Schedules.timeIn + Schedules.hourlyLoad
        lunch_start = Schedules.timeIn + Schedules.hourlyLoad
        lunch_end = Schedules.timeIn + Schedules.hourlyLoad + Schedules.lunchTime

        if self.entranceTime > lunch_start:
            raise ValueError("Entrance time is greater than lunch start")
        if self.entranceTime < lunch_start:
            raise ValueError("Entrance time is less than lunch start")
        if self.entranceTime == lunch_start:
            return True

        if self.exitTime > lunch_end:
            raise ValueError("Exit time is greater than lunch end")
        if self.exitTime < lunch_end:
            raise ValueError("Exit time is less than lunch end")
        if self.exitTime == lunch_end:  
            return True"""
        
    def actionClockIn(self):

        self.entranceTime = datetime.now()
        self.validateStart()
        pass

    def actionClockOut(self):
        
        self.exitTime = datetime.now()
        self.validateEnd()
        pass

    def justifiedDelay(self):
        pass
