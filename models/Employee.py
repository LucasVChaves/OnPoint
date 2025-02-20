from datetime import datetime

from ..controllers import Login
from ..utils import State, IDGen 
import Clock, Schedules, Role

class Employee:
    def __init__(
                self, 
                PIN: str, 
                name: str, 
                salary: float, 
                email: str, 
                birth: datetime, 
                phone: str, 
                schedules: Schedules, 
                role: Role
                ):
        
        self.PIN: str = PIN
        self.name: str = name
        self.salary: float = salary
        self.email: str = email
        self.birth: datetime = birth
        self.phone: str = phone
        self.state: State = None # Objetc from State
        self.schedules: Schedules = schedules
        self.clock: Clock = Clock()
        self.login: Login = Login()
        self.role: Role = role
        self.id = IDGen.gen_id(self.PIN)
