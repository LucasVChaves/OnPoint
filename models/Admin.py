import Employee
from ..controllers import Cadastre
from ..utils import JSONManager, State

class Admin(Employee):
    def __init__(self):
        self.cadastre: Cadastre = Cadastre()
        self.json_manager: JSONManager = JSONManager()

    # def getUser(self, id):
    #     if self.json_manager.load_from_json() == State.ADMIN:
    #         user = Admin( 
    #                     PIN: str, 
    #                     name: str, 
    #                     salary: float, 
    #                     email: str, 
    #                     birth: datetime, 
    #                     phone: str, 
    #                     schedules: Schedules, 
    #                     role: Role
    #                     )

    def setEmployee(self, empployee):
        # Waiting DB
        pass

    def cadastre_user(self, user):
        return self.cadastre.createEmpployee(user)
    
        # user pode ser Employee ou Admin


    

        
                