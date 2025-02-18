from datetime import datetime

from ..controllers import Login
from ..utils import State 
import Clock, Schedules, Role

class Employee:
    def __init__(
                self, 
                user: str, 
                PIN: str, 
                name: str, 
                salary: float, 
                email: str, 
                birth: datetime, 
                phone: str, 
                schedules: Schedules, 
                role: Role
                ):
        
        self.user: str = user
        self.PIN: str = PIN
        self.name: str = name
        self.salary: float = salary
        self.email: str = email
        self.birth: datetime = birth
        self.phone: int = phone
        self.state: State = State() # Objetc from State
        self.schedules: Schedules = Schedules(
                                                schedules.timeIn(), 
                                                schedules.hourlyLoad(), 
                                                schedules.lunchTime(), 
                                                schedules.initialVacation(), 
                                                schedules.finishVacation()
                                            )
        self.clock: Clock = Clock()
        self.login: Login = Login()
        self.role: Role = role

