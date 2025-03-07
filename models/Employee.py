from datetime import datetime

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

from utils.State import State
from utils.IDGen import IDGen 

from Schedules import Schedules
from Clock import Clock
from Role import Role

class Employee:
    def __init__(
                self, 
                ID: str,   # Mudança para garantir que o ID correto seja passado
                PIN: str, 
                name: str, 
                salary: float, 
                email: str, 
                birth: datetime, 
                phone: str,
                state: State,
                schedules: Schedules, 
                role: Role
                ):
        
        self.id: str = ID  # Usa o ID do JSON e não o gerado
        self.PIN: str = PIN
        self.name: str = name
        self.salary: float = salary
        self.email: str = email
        self.birth: datetime = birth
        self.phone: str = phone
        self.state: State = state
        self.schedules: Schedules = schedules
        self.clock: Clock = Clock()
        self.role: Role = role

    # Getters e Setters
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

    def get_PIN(self):
        return self.PIN
    
    def set_PIN(self, PIN):
        self.PIN = PIN

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_salary(self):
        return self.salary
    
    def set_salary(self, salary):
        self.salary = salary

    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

    def get_birth(self):
        return self.birth
    
    def set_birth(self, birth):
        self.birth = birth

    def get_phone(self):
        return self.phone
    
    def set_phone(self, phone):
        self.phone = phone

    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state

    def get_schedules(self):
        return self.schedules
    
    def set_schedules(self, schedules):
        self.schedules = schedules
