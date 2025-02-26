import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

from Employee import Employee

from controllers.Cadastre import Cadastre

from utils.JSONManager import JSONManager
from utils.State import State

class Admin(Employee):
    def __init__(self):
        self.cadastre: Cadastre = Cadastre()
        self.json_manager: JSONManager = JSONManager()

    def get_employee(self, id: str):
        return self.json_manager.load_from_json('employee', id)

    def set_employee(self, employee):
        self.json_manager.save_to_json('employee', employee.get_id(), employee)

    # frequencia em % (100% do mes = 22 dias uteis)
    def fix_monthly_frequency(self, id: str, new_frequency: float):
        pass

    # vai iterar pelo clocks.json somando todas
    # as horas trabalhadas no mes corrente
    def generate_monthly_worked_hours_report(self, id: str):
        pass

    def sync_holydays_callendar(self):
        pass