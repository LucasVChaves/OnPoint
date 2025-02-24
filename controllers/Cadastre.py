import re
from datetime import datetime

from ..models import Employee, Admin, Schedules, Role
from ..utils import State, JSONManager, IDGen

class Cadastre():

    def __init__(self):
        self.users = [] # Waiting DB
        self.json_manager: JSONManager = JSONManager()
        self.id_gen: IDGen = IDGen()

    def cadastre_user(
        self,
        PIN: str, 
        name: str, 
        email: str, 
        phone: str, 
        address: str, 
        birth: datetime, 
        salary: float, 
        schedules: Schedules,  
        role: Role
        ):
        
        if not(
            self.is_valid_PIN(PIN=PIN) and 
            self.is_valid_name(name=name) and 
            self.is_valid_email(email=email) and 
            self.is_valid_phone(phone=phone) and 
            self.is_valid_adress(address=address) and 
            self.is_valid_birthday(birth=birth) and 
            self.is_valid_salary(salary=salary) and 
            self.is_valid_schedules(schedules=schedules)
            ):
            return False #usuario invalido
        
        if role == Role.ADMIN:
            new_user: Admin = Admin(
                                    PIN=PIN, 
                                    name=name, 
                                    salary=salary, 
                                    email=email, 
                                    birth=birth, 
                                    phone=phone, 
                                    schedules=schedules, 
                                    role=role
                                    )
        else:
            new_user: Employee = Employee(
                                        PIN=PIN, 
                                        name=name, 
                                        salary=salary, 
                                        email=email, 
                                        birth=birth, 
                                        phone=phone, 
                                        schedules=schedules, 
                                        role=role
                                        )
        
        # Insert new_user in DB
        return self.jsonManager.save_to_json(id=new_user.id, new_user=new_user)

    def is_valid_PIN(self, PIN):
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

    def is_valid_name(self, name):
        if isinstance(name, str):
            if name == 0:
                if len(name) < 100:
                    return True
            else:
                raise ValueError("'name' is empty")
        else:
            raise TypeError("'name' needs to be a 'str'")

    def is_valid_email(self, email):
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

    def is_valid_phone(self, phone): # DDD 9 XXXXXXXX
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

    def is_valid_adress(self, address):
        if isinstance(address, str):
            if address != 0:
                return True
            else:
                raise ValueError("'address' is empty")
        else:
            raise TypeError("'address' needs to be a 'str'")

    def is_valid_birthday(self, birth):
        if isinstance(birth, datetime):
            if birth != 0:
                return True
            else:
                raise ValueError("'birth' is empty")
        else:
            raise TypeError("'birth' needs to be a 'datetime'")

    def is_valid_salary(self, salary):
        if isinstance(salary, float):
            if salary > 0:
                return True
            else:
                raise ValueError("'salary' cannot be '0'")
        else:
            raise TypeError("'salary' needs to be a 'float'")
        
    def is_valid_hourlyload(self, hourlyLoad):
        if isinstance(hourlyLoad, datetime):
            if hourlyLoad != 0:
                return True
            else:
                raise ValueError("'hourlyLoad' is empty")
        else:
             raise TypeError("'hourlyLoad' needs to be a 'datetime'")            

    def is_valid_lunch_time(self, lunchTime):
        if isinstance(lunchTime, datetime):
            if lunchTime != 0:
                return True
            else:
                raise ValueError("'lunchTime' is empty")
        else:
            raise TypeError("'lunchTime' needs to be a 'datetime'")

    def is_valid_initial_vacation(self, initialVacation):
        if isinstance(initialVacation, datetime):
            if initialVacation != 0:
                return True
            else:
                raise ValueError("'initialVacation' is empty")
        else:
            raise TypeError("'initialVacation' needs to be a 'datetime'")

    def is_valid_finish_vacation(self, finishVacation):
        if isinstance(finishVacation, str):
            if finishVacation != 0:
                return True
            else:
                raise ValueError("'finishVacation' is empty")
        else:
            raise TypeError("'finishVacation' needs to be a 'datetime'")

    def is_valid_schedules(self, scheddules):
        try:
            return (
            self.is_valid_hourlyload(hourlyLoad=scheddules.hourlyLoad) and 
            self.is_valid_lunch_time(lunchTime=scheddules.lunchTime) and 
            self.is_valid_initial_vacation(initialVacation=scheddules.initialVacation) and 
            self.is_valid_finish_vacation(finishVacation=scheddules.finishVacation)
            )
        except Exception as e:
            raise ValueError("{e}")

