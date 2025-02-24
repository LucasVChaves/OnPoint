from datetime import datetime

class Schedules:
    def __init__(self, time_in, hourly_load, lunch_time):
        self.time_in: datetime = time_in
        self.hourly_load: datetime = hourly_load
        self.lunch_time: datetime = lunch_time
        self.initial_vacation: datetime = datetime()
        self.finish_vacation: datetime = datetime()
