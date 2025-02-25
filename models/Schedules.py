from datetime import datetime

class Schedules:
    def __init__(self, time_in, hourly_load, lunch_time):
        self.time_in: datetime = time_in
        self.hourly_load: datetime = hourly_load
        self.lunch_time: datetime = lunch_time
        self.initial_vacation: datetime = datetime()
        self.finish_vacation: datetime = datetime()

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

