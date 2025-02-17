import json
from models import Empployee, Admin


class Login():

    def __init__(self, userdb):
        self.userdb = userdb

    def actionLogin(self,user, PIN):

        #verifica se o user e pin correspondem, pode ser usado .query.filter_by() mas caso der erro, usar self.userdb.get(user) == pin"""
        
        if self.userdb == "Empployee":
            return Empployee.query.filter_by(user=user, PIN=PIN).first()
        elif self.userdb == "Admin":
            return Admin.query.filter_by(user=user, PIN=PIN).first()
        else:
            return None
        pass

    def forgotPIN(user):
        # Função para trocar senha do usuário
        pass