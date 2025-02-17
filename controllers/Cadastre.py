import json
from ..models import Empployee, Admin, State, Roles
from enum import Enum


class Cadastre():

    def __init__(self, db_file='usuarios.json'):
        self.db_file = db_file
        self.usuarios = []
        try:
            with open(self.db_file, 'r') as f:
                self.usuarios = json.load(f)
        except: (FileNotFoundError, json.JSONDecodeError)   #se der ruim com erro, talvez possa ser assim
        self.usuarios = []

    def createUser(self, user: str, PIN: str, name: str, email: str, phone: str, address: str, cpf: str, rg: str, birthday: str, admission: str, resignation: str, salary: float, hourlyLoad: float, lunchTime: float, initialVacation: str, finishVacation: str, State: State, Role: Roles):
        #"add funcionario"
        if not(self.isValidUser(user) and self.isValidPIN(PIN) and self.isValidName(name) and self.isValidEmail(email) and self.isValidPhone(phone) and self.isValidAdress(address) and self.isValidCpf(cpf) and self.isValidRg(rg) and self.isValidBirthday(birthday) and self.isValidAdmission(admission) and self.isValidResigbation(resignation) and self.isValidSalary(salary) and self.isValidHourlyload(hourlyLoad) and self.isValidLunchtime(lunchTime) and self.isValidInitialvacation(initialVacation) and self.isValidFinishvacation(finishVacation)):
            return False #usuario invalido
        new_user = {
            "user": user,
            "PIN": PIN,
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
            "cpf": cpf,
            "rg": rg,
            "birthday": birthday,
            "admission": admission,
            "resignation": resignation,
            "salary": salary,
            "hourlyLoad": hourlyLoad,
            "lunchTime": lunchTime,
            "initialVacation": initialVacation,
            "finishVacation": finishVacation,
            "status": State.value,
            "role": Role.value,
        }
        pass

    def createAdmin(self, user: str, PIN: str, name: str, email: str, phone: str, address: str, cpf: str, rg: str, birthday: str, admission: str, resignation: str, salary: float, hourlyLoad: float, lunchTime: float, initialVacation: str, finishVacation: str, State: State):
        #"add gerente"

        pass



    def isValidUser(self, user:str) -> bool:
        return isinstance(user, str) and not any(u["User"] == user for u in self.usuarios) and len(user) > 0
        pass
    def isValidPIN(self, PIN):
        return isinstance(PIN, int) and not any(u["PIN"] == PIN for u in self.usuarios) and len(PIN) > 0
        pass
    def isValidName(self, name):
        return isinstance(name, str) and not any(u["Name"] == name for u in self.usuarios) and len(name) > 0
        pass
    def isValidEmail(self, email):
        return "@" in email and "." in email and not any(u["email"] == email for u in self.usuarios) #ve se o email ja existe e se é valido
        pass
    def isValidPhone(phone):
        return phone.isdigit() and len(phone) > 0
        pass
    def isValidAdress(address):
        return isinstance(address, str) and len(address) > 0
        pass
    def isValidCpf(cpf):
        return isinstance(cpf, int) and len(cpf) > 0
        pass
    def isValidRg(rg):
        return isinstance(rg, int) and len(rg) > 0
        pass
    def isValidBirthday(birthday):
        return isinstance(birthday, str) and len(birthday.split("-")) == 3 #a data tem que estar no formato dia-mes-ano
        pass
    def isValidAdmission(admission):
        return isinstance(admission, str) and len(admission) > 0
        pass
    def isValidResigbation(resignation):
        return isinstance(resignation, str) and len(resignation) > 0
        pass
    def isValidSalary(salary):
        return isinstance(salary, float) and len(salary) > 0
        pass
    def isValidHourlyload(hourlyLoad):
        return isinstance(hourlyLoad, int) and len(hourlyLoad) > 0
        pass
    def isValidLunchtime(lunchTime):
        return isinstance(lunchTime, int) and len(lunchTime) > 0
        pass
    def isValidInitialvacation(initialVacation):
        return isinstance(initialVacation, str) and len(initialVacation) > 0
        pass
    def isValidFinishvacation(finishVacation):
        return isinstance(finishVacation, str) and len(finishVacation) > 0
        pass

