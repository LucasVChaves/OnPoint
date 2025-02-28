from datetime import datetime, timedelta
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

from models.Schedules import Schedules
from utils.JSONManager import JSONManager
from utils.State import State

class Clock():
    def __init__(self):
        self.entrance_time: datetime = None
        self.lunch_complete: bool = False
        self.lunch_start: datetime = None
        self.json_manager = JSONManager()

    # Getter and Setter
    def get_entrance_time(self):
        return self.entrance_time
    
    def set_entrance_time(self, entrance_time):
        self.entrance_time = entrance_time

    def get_lunch_complete(self):
        return self.lunch_complete
    
    def set_lunch_complete(self, lunch_complete):
        self.lunch_complete = lunch_complete

    def get_lunch_start(self):
        return self.lunch_start
    
    def set_lunch_start(self, lunch_start):
        self.lunch_start = lunch_start

    def action_clock(self, employee_id: str, state: State):
        now = datetime.now()
        print(f"[DEBUG] ID recebido para bater ponto: {employee_id}")

        # Buscar funcionário pelo ID correto
        all_employees = self.json_manager.load_all_from_json("employee")
        employee_data = next((emp for emp in all_employees if str(emp["id"]) == str(employee_id)), None)

        if not employee_data:
            raise ValueError(f"Funcionário com ID {employee_id} não encontrado.")

        # Certificando-se de que employee_id está correto
        employee_id = employee_data["id"]  # Garantindo que estamos utilizando o ID correto do funcionário

        # Buscar horário do funcionário pelo ID correto
        all_schedules = self.json_manager.load_all_from_json("schedules")
        schedule_data = next((sch for sch in all_schedules if str(sch["id"]) == str(employee_id)), None)

        if not schedule_data:
            raise ValueError(f"Horário para o funcionário {employee_data['name']} ({employee_id}) não encontrado.")

        # Extraindo os horários do JSON
        time_in = datetime.strptime(schedule_data["time_in"], "%H:%M:%S").time()
        hourly_load = datetime.strptime(schedule_data["hourly_load"], "%H:%M:%S").time()
        lunch_time = datetime.strptime(schedule_data["lunch_time"], "%H:%M:%S").time()

        high_limit = datetime.combine(datetime.today(), time_in) - timedelta(minutes=15)
        low_limit = datetime.combine(datetime.today(), time_in) + timedelta(minutes=15)

        # Validando Entrada
        match state:
            case State.OUT_WORK:
                if not (high_limit <= now <= low_limit):
                    raise ValueError("Entrando fora do horário proposto!")

                schedule_data["clock_ins"].append(now.strftime("%H:%M:%S"))
                self.json_manager.save_to_json("schedules", employee_id, schedule_data)
                return True

            case State.WORKING:
                schedule_data["clock_outs"].append(now.strftime("%H:%M:%S"))

                if self.lunch_complete:
                    expected_exit_time = self.entrance_time + timedelta(
                        hours=hourly_load.hour, 
                        minutes=hourly_load.minute
                    ) + timedelta(hours=lunch_time.hour)

                    if now == expected_exit_time:
                        self.entrance_time = None
                        self.lunch_start = None
                        self.lunch_complete = False
                        self.json_manager.save_to_json("schedules", employee_id, schedule_data)
                        return True
                    elif now > expected_exit_time:
                        raise ValueError("Saindo mais tarde")
                    else:
                        raise ValueError("Saindo mais cedo")
                else:
                    raise ValueError("Almoço não completo!")

            case _:
                raise ValueError("Estado inválido")

    def action_lunch(self, employee_id: str, state: State):
        now = datetime.now()
        
        # Buscar horário do funcionário pelo ID correto
        all_schedules = self.json_manager.load_all_from_json("schedules")
        schedule_data = next((sch for sch in all_schedules if str(sch["id"]) == str(employee_id)), None)

        if not schedule_data:
            raise ValueError(f"Horário do funcionário com ID {employee_id} não encontrado.")

        lunch_time = datetime.strptime(schedule_data["lunch_time"], "%H:%M:%S").time()

        # Validando
        match state:
            case State.WORKING:
                if not self.lunch_start:
                    if not self.lunch_complete:
                        self.lunch_start = now
                        return True
                    else:
                        raise ValueError("Hora de almoço já foi completada.")
                else:
                    raise ValueError("Horário de almoço já foi iniciado.")

            case State.LUNCH:
                lunch_duration = now - self.lunch_start
                expected_lunch_time = timedelta(hours=lunch_time.hour, minutes=lunch_time.minute)

                if lunch_duration >= expected_lunch_time:
                    self.lunch_complete = True
                    return True
                else:
                    raise ValueError("Hora de almoço incompleta.")

            case _:
                raise ValueError("Estado inválido")

    def justified_clock(self):
        pass
