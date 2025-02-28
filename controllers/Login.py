import smtplib
import random
import string
import sys
import os

from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

from models.Employee import Employee
from models.Admin import Admin
from models.Schedules import Schedules
from models.Role import Role  # Importação corrigida
from utils.State import State  # Adicionando o import correto para o Enum State

from utils.JSONManager import JSONManager


class Login:
    def __init__(self):
        self.json_manager: JSONManager = JSONManager()

    def action_login(self, id, PIN):
        employee_data = self.json_manager.load_from_json('employee', id)

        if not employee_data:
            raise ValueError("Usuário não encontrado!")

        if employee_data['pin'] == PIN:
            try:
                schedules_data = self.json_manager.load_from_json('schedules', id)
            except IndexError as e:
                print(e)

            schedules = Schedules(
                datetime.strptime(schedules_data['time_in'], "%H:%M:%S").time(),
                datetime.strptime(schedules_data['hourly_load'], "%H:%M:%S").time(),
                datetime.strptime(schedules_data['lunch_time'], "%H:%M:%S").time(),
                datetime.strptime(schedules_data['initial_vacation'], "%d/%m/%Y"),
                datetime.strptime(schedules_data['finish_vacation'], "%d/%m/%Y"),
                schedules_data.get("clock_ins", []),  # Adicionando clock_ins
                schedules_data.get("clock_outs", [])  # Adicionando clock_outs
            )

            try:
                # Tentando converter o estado para o Enum State
                state_str = employee_data['state']
                state = State.__members__.get(state_str.upper() if isinstance(state_str, str) else state_str, State.INITIAL)

            except KeyError:
                # Caso o estado não seja encontrado, atribuímos um valor padrão
                print(f"[DEBUG] Estado inválido {employee_data['state']}, atribuindo estado 'Initial'.")
                state = State.INITIAL  # Valor padrão para estado

            if employee_data['role'] == 'Admin':
                return Admin(
                    id=employee_data['id'],  # Corrigido para passar o id
                    PIN=employee_data['pin'],
                    name=employee_data['name'],
                    salary=float(employee_data['salary']),
                    email=employee_data['email'],
                    birth=datetime.strptime(employee_data['birth'], "%d/%m/%Y"),
                    phone=employee_data['phone'],
                    state=state,  # Passando o estado como enum
                    schedules=schedules,
                    role=Role.ADMIN  # Corrigido para passar um objeto Role válido
                )
            else:
                return Employee(
                    ID=employee_data['id'],  # Corrigido para garantir que ID seja passado
                    PIN=employee_data['pin'],
                    name=employee_data['name'],
                    salary=float(employee_data['salary']),
                    email=employee_data['email'],
                    birth=datetime.strptime(employee_data['birth'], "%d/%m/%Y"),
                    phone=employee_data['phone'],
                    state=state,  # Passando o estado como enum
                    schedules=schedules,
                    role=Role.EMPLOYEE  # Corrigido para passar um objeto Role válido
                )
        else:
            raise ValueError("ID ou PIN incorretos")

    def forgot_PIN(self, id):
        # Busca o usuário baseado no id
        user = self.json_manager.load_from_json(category="employee", id=id)

        if user:
            # Cria uma nova senha
            new_pin = ''.join(random.choices(string.digits, k=8))
            user["pin"] = new_pin
            self.json_manager.save_to_json(category="employee", id=id, new_object=user)

            msg = MIMEMultipart()
            msg['From'] = 'noreply@gmail.com'
            msg['To'] = user["email"]
            msg['Subject'] = 'Your new PIN'

            body = f'Hello {user["name"]},\n\nYour new PIN is: {new_pin}\n\nBest regards,\nOn Point Team'
            msg.attach(MIMEText(body, 'plain'))

            try:
                # Simulação de envio de e-mail (requer credenciais válidas)
                server = smtplib.SMTP('smtp.example.com', 587)
                server.starttls()
                server.login('your_email@example.com', 'your_password')
                text = msg.as_string()
                server.sendmail('your_email@example.com', user["email"], text)
                server.quit()
                print("Email sent successfully")
            except Exception as e:
                print(f"Failed to send email: {e}")
        else:
            raise ValueError(f"Usuário não encontrado! ID: {id}")
