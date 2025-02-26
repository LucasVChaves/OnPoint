import smtplib
import random
import string
import sys
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

from models.Employee import Employee
from models.Admin import Admin

from utils.JSONManager import JSONManager


class Login():

    def __init__(self):
        self.json_manager: JSONManager = JSONManager()

    def action_login(self,id, PIN):
        
        # Busca o usuário baseado no id
        user = self.json_manager.load_from_json(category="employee",id=id)

        if PIN == user.get_PIN():
            return True
        else:
            raise ValueError("PIN ERRADA!")

    def forgot_PIN(self, id):
        # Busca o usuário baseado no id
        if self.json_manager.load_from_json(category="employee",id=id):
            user = self.json_manager.load_from_json(category="employee",id=id)

            # Cria uma senha nova
            new_pin = ''.join(random.choices(string.digits, k=8))
            user.set_PIN(new_pin)
            self.json_manager.save_to_json(category="employee", id=id, new_object=user)

            msg = MIMEMultipart()
            msg['From'] = 'noreply@gmail.com'
            msg['To'] = user.get_email()
            msg['Subject'] = 'Your new PIN'

            body = f'Hello {user},\n\nYour new PIN is: {new_pin}\n\nBest regards,\nOn Point Team'
            msg.attach(MIMEText(body, 'plain'))

            try:  # manda email,precisa de um email e senha para funcionar******
                server = smtplib.SMTP('smtp.example.com', 587)
                server.starttls()
                server.login('your_email@example.com', 'your_password')
                text = msg.as_string()
                server.sendmail('your_email@example.com', user.email, text)
                server.quit()
                print("Email sent successfully")
            except Exception as e:
                print(f"Failed to send email: {e}")
        else:
            raise ValueError("Usuário não encontrado! \nID: {id}.")