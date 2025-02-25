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
        return (self.jsonManager.save_to_json(category="employee",id=new_user.get_id(), new_object=new_user) and 
                self.json_manager.save_to_json(category="schedules", id=new_user.get_id(), new_object=new_user.get_schedules()) and
                self.json_manager.save_tojson(category="role", id=new_user.get_id(), new_object=new_user.get_role()))


    def is_valid_PIN(self, PIN):
        # Verifica se PIN é uma str
        if isinstance(PIN, str):
            # Verifica se PIN contém algo
            if PIN != 0:
                # Verifica se o tamanho é o correto
                if len(PIN) == 8:
                    return True
                else:
                    raise ValueError("'PIN' needs to have 8 number")
            else:
                raise ValueError("'PIN' is empty")
        else:
            raise TypeError("'PIN' needs to be a 'str'")

    def is_valid_name(self, name):
        # Verifica se name é uma str
        if isinstance(name, str):
            # Verifica se name contém algo
            if name != 0:
                # Verifica se o tamanho é o correto
                if len(name) < 100:
                    return True
            else:
                raise ValueError("'name' is empty")
        else:
            raise TypeError("'name' needs to be a 'str'")

    def is_valid_email(self, email):
        # Verifica se email é um str
        if isinstance(email, str):
            # Verifica se email é do tamanho correto
            if len(email) != 0:
                # Verifica se está no padrão de email: XXXX@tanana.com
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
        # Verifica se phone é str
        if isinstance(phone, str):
            # Verifica se phone está vazio
            if phone != 0:
                # Verifica se o tamanho é o correto
                if len(phone) == 11:
                    return True
                else:
                    raise ValueError("'phone' needs to have 11 characteres")
            else:
                raise ValueError("'phone' cannot be '0'")
        else:
            raise TypeError("'phone' needs to be a 'str'")

    def is_valid_adress(self, address):
        # Verifica se address é uma str
        if isinstance(address, str):
            # Verifica se address está vazio
            if address != 0:
                return True
            else:
                raise ValueError("'address' is empty")
        else:
            raise TypeError("'address' needs to be a 'str'")

    def is_valid_birthday(self, birth):
        # Verifica se birth é um datetime
        if isinstance(birth, datetime):
            # Verifica se está vazio
            if birth != 0:
                return True
            else:
                raise ValueError("'birth' is empty")
        else:
            raise TypeError("'birth' needs to be a 'datetime'")

    def is_valid_salary(self, salary):
        # Verifica se salary é um float
        if isinstance(salary, float):
            # Verifica se salary é maior que 0
            if salary > 0:
                return True
            else:
                raise ValueError("'salary' cannot be '0'")
        else:
            raise TypeError("'salary' needs to be a 'float'")
        
    def is_valid_hourlyload(self, hourly_load):
        # Verifica se hourly_load é um datetime
        if isinstance(hourly_load, datetime):
            # Verifica se está vazio
            if hourly_load != 0:
                return True
            else:
                raise ValueError("'hourlyLoad' is empty")
        else:
             raise TypeError("'hourlyLoad' needs to be a 'datetime'")            

    def is_valid_lunch_time(self, lunch_time):
        # Verifica se lunch_time é um datetime
        if isinstance(lunch_time, datetime):
            # Verifica se lunch_time está vazio
            if lunch_time != 0:
                return True
            else:
                raise ValueError("'lunchTime' is empty")
        else:
            raise TypeError("'lunchTime' needs to be a 'datetime'")

    def is_valid_schedules(self, scheddules):
        try:
            return (
            self.is_valid_hourlyload(hourlyLoad=scheddules.get_hourly_load()) and 
            self.is_valid_lunch_time(lunchTime=scheddules.get_lunch_Time())
            )
        except Exception as e:
            raise ValueError("{e}")

