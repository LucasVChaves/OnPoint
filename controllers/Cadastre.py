import json
from ..models import Empployee, Admin
from enum import Enum

class Cadastre():

    def createEmpployee(self, user: str, PIN: str, name: str, email: str, phone: str, address: str, cpf: str, rg: str, birthday: str, admission: str, resignation: str, salary: float, hourlyLoad: float, lunchTime: float, initialVacation: str, finishVacation: str, status: str):
        "add funcionario"
        if not(self.isValidUser(user) and self.isValidPIN(PIN) and self.isValidName(name) and self.isValidEmail(email) and self.isValidPhone(phone) and self.isValidAdress(address) and self.isValidCpf(cpf) and self.isValidRg(rg) and self.isValidBirthday(birthday) and self.isValidAdmission(admission) and self.isValidResigbation(resignation) and self.isValidSalary(salary) and self.isValidHourlyload(hourlyLoad) and self.isValidLunchtime(lunchTime) and self.isValidInitialvacation(initialVacation) and self.isValidFinishvacation(finishVacation)):
            return False
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
            "status": "active"
        }
        pass

    def createAdmin(user):
        pass

    def isValidUser(self, user:str) -> bool:
        return isinstance(user, str) and len(user) > 0
        pass
    def isValidPIN(PIN):
        return isinstance(PIN, int) and len(PIN) > 0
        pass
    def isValidName(name):
        return isinstance(name, str) and len(name) > 0
        pass
    def isValidEmail(email):
        return "@" in email and "." in email and not any(u["email"] == email for u in self.usuarios)
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
        return isinstance(birthday, str) and len(birthday) > 0
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

