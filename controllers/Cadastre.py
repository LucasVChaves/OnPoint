import re
from datetime import datetime

from ..models import Employee, Admin, Schedules, Role
from ..utils import State, JSONManager, IDGen

class Cadastre():

    def __init__(self):
        self.users = [] # Waiting DB
        self.jsonManager: JSONManager = JSONManager()
        self.idGen: IDGen = IDGen()

    def cadastreUser(
        self,
        PIN: str, 
        name: str, 
        email: str, 
        phone: str, 
        address: str, 
        birth: datetime, 
        salary: float, 
        schedules: Schedules, 
        state: State, 
        role: Role
        ):
        
        if not(
            self.isValidPIN(PIN=PIN) and 
            self.isValidName(name=name) and 
            self.isValidEmail(email=email) and 
            self.isValidPhone(phone=phone) and 
            self.isValidAdress(address=address) and 
            self.isValidBirthday(birth=birth) and 
            self.isValidSalary(salary=salary) and 
            self.isValidSchedules(schedules=schedules)
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
                                         
        # new_user = {
        #     "user": user,
        #     "PIN": PIN,
        #     "name": name,
        #     "email": email,
        #     "phone": phone,
        #     "address": address,
        #     "birthday": birthday,
        #     "salary": salary,
        #     "hourlyLoad": schedules.hourlyLoad(),
        #     "lunchTime": schedules.lunchTime(),
        #     "initialVacation": schedules.initialVacation(),
        #     "finishVacation": schedules.finishVacation(),
        #     "status": state.value, 
        #     "role": role.value,
        # }
        
        # Insert new_user in DB
        return self.jsonManager.save_to_json(id=new_user.id, new_user=new_user)

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
            self.isValidHourlyload(hourlyLoad=scheddules.hourlyLoad) and 
            self.isValidLunchtime(lunchTime=scheddules.lunchTime) and 
            self.isValidInitialvacation(initialVacation=scheddules.initialVacation) and 
            self.isValidFinishvacation(finishVacation=scheddules.finishVacation)
            )
        except Exception as e:
            raise ValueError("{e}")

