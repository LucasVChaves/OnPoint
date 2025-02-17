from datetime import datetime

from ..controllers import Login
from ..utils import State 
import Clock, Schedules

class Employee:
    def __init__(self, user, PIN, name, salary, email, birth, phone, schedules, status):
        self.user: str = user
        self.PIN: int = PIN
        self.name: str = name
        self.salary: float = salary
        self.email: str = email
        self.birth: datetime = birth
        self.phone: int = phone
        self.state: State = State() # Objetc from State
        self.schedules: Schedules = Schedules(schedules.getTimeIn(), schedules.getHourlyLoad(), schedules.getLunchTime(), schedules.getInitialVacation(), schedules.getFinishVacation()) # Object from Schedules
        self.clock: Clock = Clock()
        self.login: Login = Login()
        self.status: str = status

