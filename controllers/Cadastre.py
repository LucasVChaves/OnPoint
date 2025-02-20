import json
import re
from enum import Enum
from datetime import datetime

from ..models import Employee, Admin
from ..utils import State, Schedules, Role


class Cadastre():

    def __init__(self):
        self.users = [] # Waiting DB

    def createUser(
        self, 
        user: str, 
        PIN: str, 
        name: str, 
        email: str, 
        phone: str, 
        address: str, 
        birthday: datetime, 
        salary: float, 
        schedules: Schedules, 
        state: State, 
        role: Role
        ):
        
        if not(
            self.isValidUser(user) and 
            self.isValidPIN(PIN) and 
            self.isValidName(name) and 
            self.isValidEmail(email) and 
            self.isValidPhone(phone) and 
            self.isValidAdress(address) and 
            self.isValidBirthday(birthday) and 
            self.isValidSalary(salary) and 
            self.isValidSchedules(schedules)
            ):
            return False #usuario invalido
        new_user = {
            "user": user,
            "PIN": PIN,
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
            "birthday": birthday,
            "salary": salary,
            "hourlyLoad": schedules.hourlyLoad(),
            "lunchTime": schedules.lunchTime(),
            "initialVacation": schedules.initialVacation(),
            "finishVacation": schedules.finishVacation(),
            "status": state.value, 
            "role": role.value,
        }
        
        # Insert new_user in DB

    def isValidUser(self, user:str) -> bool:
        if isinstance(user, str):
            if len(user) >= 5 and len(user) <= 50:
                #TODO Need to better
                for user_name in self.users:
                    if user.name == user_name:
                        raise ValueError("{user} already exists in DB")

                return True
            else:
                raise ValueError("'user' needs to be beetwen 5 and 50 characters")
        else:
            raise TypeError("'user' needs to be a 'str'")

    def isValidPIN(self, PIN):
        if isinstance(PIN, str):
            if PIN == 0:
                if len(PIN) == 8:
                    return True
                else:
                    raise ValueError("'PIN' needs to have 8 number")
            else:
                raise ValueError("'PIN' is empty")
        else:
            raise TypeError("'PIN' needs to be a 'str'")

    def isValidName(self, name):
        if isinstance(name, str):
            if name == 0:
                if len(name) < 100:
                    return True
            else:
                raise ValueError("'name' is empty")
        else:
            raise TypeError("'name' needs to be a 'str'")

    def isValidEmail(self, email):
        if isinstance(email, str):
            if len(email) == 0:
                padrao = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" # Identfy if a email is correct
                try:
                    return bool(re.match(padrao, email))
                except Exception as e:
                        return e
            else:
                raise ValueError("'email' is empty")
        else:
            raise TypeError("'email' needs to be a 'str'")

    def isValidPhone(self, phone): # DDD 9 XXXXXXXX
        if isinstance(phone, str):
            if phone == 0:
                if len(phone) == 11:
                    return True
                else:
                    raise ValueError("'phone' needs to have 11 characteres")
            else:
                raise ValueError("'phone' cannot be '0'")
        else:
            raise TypeError("'phone' needs to be a 'str'")

    def isValidAdress(self, address):
        if isinstance(address, str):
            if address != 0:
                return True
            else:
                raise ValueError("'address' is empty")
        else:
            raise TypeError("'address' needs to be a 'str'")

    def isValidBirthday(self, birth):
        if isinstance(birth, datetime):
            if birth != 0:
                return True
            else:
                raise ValueError("'birth' is empty")
        else:
            raise TypeError("'birth' needs to be a 'datetime'")

    def isValidSalary(self, salary):
        if isinstance(salary, float):
            if salary > 0:
                return True
            else:
                raise ValueError("'salary' cannot be '0'")
        else:
            raise TypeError("'salary' needs to be a 'float'")
        
    def isValidHourlyload(self, hourlyLoad):
        if isinstance(hourlyLoad, datetime):
            if hourlyLoad != 0:
                return True
            else:
                raise ValueError("'hourlyLoad' is empty")
        else:
             raise TypeError("'hourlyLoad' needs to be a 'datetime'")            

    def isValidLunchtime(self, lunchTime):
        if isinstance(lunchTime, datetime):
            if lunchTime != 0:
                return True
            else:
                raise ValueError("'lunchTime' is empty")
        else:
            raise TypeError("'lunchTime' needs to be a 'datetime'")

    def isValidInitialvacation(self, initialVacation):
        if isinstance(initialVacation, datetime):
            if initialVacation != 0:
                return True
            else:
                raise ValueError("'initialVacation' is empty")
        else:
            raise TypeError("'initialVacation' needs to be a 'datetime'")

    def isValidFinishvacation(self, finishVacation):
        if isinstance(finishVacation, str):
            if finishVacation != 0:
                return True
            else:
                raise ValueError("'finishVacation' is empty")
        else:
            raise TypeError("'finishVacation' needs to be a 'datetime'")

    def isValidSchedules(self, scheddules):
        try:
            return (
            self.isValidHourlyload(scheddules.hourlyLoad) and 
            self.isValidLunchtime(scheddules.lunchTime) and 
            self.isValidInitialvacation(scheddules.initialVacation) and 
            self.isValidFinishvacation(scheddules.finishVacation)
            )
        except Exception as e:
            print("{e}")

