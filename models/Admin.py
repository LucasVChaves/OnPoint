import sys
import os
from Employee import Employee
from utils.JSONManager import JSONManager
from datetime import datetime, timedelta

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

class Admin(Employee):
    def __init__(self):
        self.json_manager: JSONManager = JSONManager()

    def get_employee(self, id: str):
        return self.json_manager.load_from_json('employee', id)

    def set_employee(self, employee):
        self.json_manager.save_to_json('employee', employee.get_id(), employee)

    # adiciona correction dias ao clock out, ou seja funcionario faltou 3 dias com atestado
    # e o adm faz a correcao, eh adicionado 3 novos clock_outs pro historico
    # arrumando a frequencia tanto pro json em si quanto pro generate_monthly_worked_hours
    def fix_monthly_frequency(self, id: str, correction: int):
        if correction <= 0:
            raise ValueError(f"Correction has to be > 0, invalid val {correction}")
        
        employee = Employee(**self.json_manager.load_from_json('employee', id))
        schedule = employee.get_schedules()
        # range: [0, n) entao eh preciso + 1
        for _ in range(correction + 1):
            schedule.append_clock_outs(schedule.get_time_in())

    def generate_monthly_worked_hours(self, id: str):
        employee = Employee(**self.json_manager.load_from_json('employee', id))
        schedule = employee.get_schedules()

        total_worked_hours = 0
        clock_outs = schedule.get_clock_outs()
        clock_ins = schedule.get_clock_ins()
        # usa o clock_outs como base pois eh possivel que
        # clock_ins.len > clock_outs.len se ainda estiver em turno
        for i in clock_outs:
            worked_hours = datetime.strptime(clock_outs[i], "%H:%M:%S") - datetime.strptime(clock_ins[i], "%H:%M:%S")
            total_worked_hours += worked_hours
        
        return total_worked_hours


    def sync_holydays_callendar(self, id: str, start_date: datetime, end_date: datetime):
        employee = Employee(**self.json_manager.load_from_json('employee', id))
        schedule = employee.get_schedules()

        schedule.set_initial_vacation = start_date
        schedule.set_finish_vacation = end_date
        pass