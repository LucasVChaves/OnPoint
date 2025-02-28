import sys
import os
from models.Employee import Employee
from utils.JSONManager import JSONManager
from datetime import datetime

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

class Admin(Employee):
    def __init__(self, id, PIN, name, salary, email, birth, phone, state, schedules, role):
        # Aqui passamos o ID correto para a classe Employee
        super().__init__(ID=id, PIN=PIN, name=name, salary=salary, email=email, 
                         birth=birth, phone=phone, state=state, schedules=schedules, role=role)
        self.json_manager = JSONManager()

    def get_employee(self, id: str):
        return self.json_manager.load_from_json('employee', id)

    def set_employee(self, employee):
        self.json_manager.save_to_json('employee', employee.get_id(), employee)

    # Adiciona dias de correção ao clock_out (Ex: funcionário faltou com atestado)
    def fix_monthly_frequency(self, id: str, correction: int):
        if correction <= 0:
            raise ValueError(f"Correction has to be > 0, invalid value {correction}")
        
        employee = Employee(**self.json_manager.load_from_json('employee', id))
        schedule = employee.get_schedules()
        for _ in range(correction + 1):
            schedule.append_clock_outs(schedule.get_time_in())

    # Gera relatório de horas trabalhadas no mês
    def generate_monthly_worked_hours(self, id: str):
        employee = Employee(**self.json_manager.load_from_json('employee', id))
        schedule = employee.get_schedules()

        total_worked_hours = 0
        clock_outs = schedule.get_clock_outs()
        clock_ins = schedule.get_clock_ins()

        # Usa clock_outs como base para cálculo de horas
        for i in range(len(clock_outs)):
            worked_hours = datetime.strptime(clock_outs[i], "%H:%M:%S") - datetime.strptime(clock_ins[i], "%H:%M:%S")
            total_worked_hours += worked_hours.total_seconds() / 3600  # Converte para horas
        
        return total_worked_hours

    # Atualiza o calendário de férias do funcionário
    def sync_holidays_calendar(self, id: str, start_date: datetime, end_date: datetime):
        employee = Employee(**self.json_manager.load_from_json('employee', id))
        schedule = employee.get_schedules()

        schedule.set_initial_vacation(start_date)
        schedule.set_finish_vacation(end_date)
