from datetime import datetime

from ..controllers import Login
from ..utils import State, Schedules
import Clock

class Empployee:
    def __init__(self, user, PIN, name, salary, email, birth, phone, schedules):
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

    # Getters

    def getUser(self):
        return self.user
        
    def getPIN(self):
        return self.PIN

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary

    def getEmail(self):
        return self.email
    
    def getbirth(self):
        return self.birth

    def getPhone(self):
        return self.phone

    def getState(self):
        return self.state

    def getSchedules(self):
        return self.schedules

    # Setters

    def setUser(self, user):
        self.user = user

    def setPIN(self, PIN):
        self.PIN = PIN

    def setName(self, name):
        self.name = name

    def setSalary(self, salary):
        self.salary = salary

    def setEmail(self, email):
        self.email = email

    def setBirth(self, birth):
        self.birth = birth

    def setPhone(self, phone):
        self.phone = phone

    def setState(self, state):
        self.state = state

    def setSchedules(self, schedules):
        self.schedules = schedules
        



    
