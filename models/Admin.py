import Employee
from ..controllers import Cadastre

class Admin(Employee):
    def __init__(self):
        self.cadastre: Cadastre = Cadastre()

    def getEmployee(self, empployee):
        # Waiting DB
        pass

    def setEmployee(self, empployee):
        # Waiting DB
        pass

    def cadastreEmpployee(self, empployee):
        return self.cadastre.createEmpployee(empployee)
    
    def cadastreAdmin(self, admin):
        return self.cadastre.createAdmin(admin)


    

        
                