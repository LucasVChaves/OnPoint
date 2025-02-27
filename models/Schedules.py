from datetime import datetime

class Schedules:
    def __init__(self, 
                    time_in: datetime.time, 
                    hourly_load: datetime.time, 
                    lunch_time: datetime.time, 
                    initial_vacation: datetime, 
                    finish_vacation: datetime,
                    clock_ins: list[datetime.time], # horario que bateu ponto para entrar
                    clock_outs: list[datetime.time] # horario que bateu pinto pra sair
                    ):
        self.time_in: datetime = time_in
        self.hourly_load: datetime = hourly_load
        self.lunch_time: datetime = lunch_time
        self.initial_vacation: datetime = initial_vacation
        self.finish_vacation: datetime = finish_vacation
        self.clock_ins: list[datetime.time] = clock_ins
        self.clock_outs: list[datetime.time] = clock_outs

    # getter and setters
    def get_time_in(self):
        return self.time_in

    def set_time_in(self, time_in):
        self.time_in = time_in

    def get_hourly_load(self):
        return self.hourly_load

    def set_hourly_load(self, hourly_load):
        self.hourly_load = hourly_load

    def get_lunch_time(self):
        return self.lunch_time

    def set_lunch_time(self, lunch_time):
        self.lunch_time = lunch_time

    def get_initial_vacation(self):
        return self.initial_vacation

    def set_initial_vacation(self, initial_vacation):
        self.initial_vacation = initial_vacation

    def get_finish_vacation(self):
        return self.finish_vacation

    def set_finish_vacation(self, finish_vacation):
        self.finish_vacation = finish_vacation

    # retorna List!
    def get_clock_ins(self):
        return self.clock_ins
    
    def append_clock_ins(self, curr_time: datetime.time):
        self.clock_ins.append(curr_time)

    # retorna List!
    def get_clock_out(self):
        return self.clock_outs
    
    def append_clock_outs(self, curr_time: datetime.time):
        self.clock_outs.append(curr_time)