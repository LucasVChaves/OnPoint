from Employee import Employee
from ..controllers import Cadastre
from ..utils import JSONManager, State

class Admin(Employee):
    def __init__(self):
        self.cadastre: Cadastre = Cadastre()
        self.json_manager: JSONManager = JSONManager()

    def set_employee(self, employee):
        self.json_manager.save_to_json('employee', employee.get_id(), employee)
