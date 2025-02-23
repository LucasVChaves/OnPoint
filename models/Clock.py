from datetime import datetime
import Schedules


class Clock():
    def __init__(self):
        self.entrance_time: datetime = datetime()
        self.lunch_time: datetime = datetime()

    #TODO Refazer função para tratar erro (talvez)
    #TODO Melhorar validação, como validação de estados (Férias, doente, etc)

    # No lugar de "self.entrance_time", colocar apenas hora atual
    def validate_start(self, schedules: Schedules):
        work_start = schedules.timeIn
        
        if self.entrance_time > work_start:
            raise ValueError("Entrance time is greater than work start")
        if self.entrance_time < work_start:
            raise ValueError("Entrance time is less than work start")
        if self.entrance_time == work_start:
            return True

    #TODO Refazer função para tratar erro (talvez)
    #TODO Melhorar validação, como validação de estados (Férias, doente, etc)

    #OBS: Trocar "exitTime" por hora atual
    def validate_end(self, schedules: Schedules):

        work_end = self.entrance_time + schedules.hourlyLoad + schedules.lunchTime
        overtime = exitTime - work_end

        if self.exitTime > work_end:
            raise ValueError("Exit time is {overtime} hour(s) after than work end")
        if self.exitTime < work_end:
            raise ValueError("Exit time is {overtime} hour(s) before than work end")
        if self.exitTime == work_end:
            return True

    #TODO Refazer a função inteiro pq nada faz sentido! (Aceito réplicas)
    #TODO Fazer apenas a verificação de estados, e verificar se o funcionário já almoçou
    def validate_lunch_intial(self, schedules: Schedules):
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
            return True
        
    def validate_lunch_finish(self, schedules: Schedules):
        pass
        
    def action_clock_in(self):
        self.validateStart()
        self.entranceTime = datetime.now()

    def action_clock_out(self):
        self.validateEnd()
        self.exitTime = datetime.now()
        
    def justified_clock(self):
        pass
