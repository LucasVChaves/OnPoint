from datetime import datetime

class Schedules:
    def __init__(self, time_in, hourly_load, lunch_time, initial_vacation, finish_vacation):
        self.time_in: datetime = time_in
        self.hourly_load: datetime = hourly_load
        self.lunch_time: datetime = lunch_time
        self.initial_vacation: datetime = initial_vacation
        self.finish_vacation: datetime = finish_vacation
