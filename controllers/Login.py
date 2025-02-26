import smtplib
import random
import string
import sys
import os

from datetime import datetime
from datetime import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

from models.Employee import Employee
from models.Admin import Admin
from models.Schedules import Schedules

from utils.JSONManager import JSONManager


class Login():

    def __init__(self):
        self.json_manager: JSONManager = JSONManager()

    def action_login(self,id, PIN):
        
        if self.json_manager.load_from_json('employee', id)['pin'] == PIN:

            try:
                user = self.json_manager.load_from_json('employee', id)
                schedules = self.json_manager.load_from_json('schedules', id)
            except IndexError as e:
                print(e)

            if self.json_manager.load_from_json('employee', id)['role'] == 'admin':

                return Admin(PIN=user['pin'],
                                name=user['name'],
                                salary=float(user['salary']),
                                email=user['email'],
                                birth=datetime.strptime(user['birth'],"%d/%m/%Y"),
                                phone=user['phone'],
                                state=user['state'],
                                schedules=Schedules(datetime.strptime(schedules['time_in'], "%H:%M:%S").time(),
                                                    datetime.strptime(schedules['hourly_load'], "%H:%M:%S").time(),
                                                    datetime.strptime(schedules['lunch_time'], "%H:%M:%S").time(),
                                                    datetime.strptime(schedules['initial_vacation'], "%d/%m/%Y"),
                                                    datetime.strptime(schedules['finish_vacation'], "%d/%m/%Y")),
                                role=user['role'])
            else:

                return Employee(PIN=user['pin'],
                                name=user['name'],
                                salary=float(user['salary']),
                                email=user['email'],
                                birth=datetime.strptime(user['birth'],"%d/%m/%Y"),
                                phone=user['phone'],
                                state=user['state'],
                                schedules=Schedules(datetime.strptime(schedules['time_in'], "%H:%M:%S").time(),
                                                    datetime.strptime(schedules['hourly_load'], "%H:%M:%S").time(),
                                                    datetime.strptime(schedules['lunch_time'], "%H:%M:%S").time(),
                                                    datetime.strptime(schedules['initial_vacation'], "%d/%m/%Y"),
                                                    datetime.strptime(schedules['finish_vacation'], "%d/%m/%Y")),
                                role=user['role'])


        else:
            raise ValueError("ID ou PIN incorretos")

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