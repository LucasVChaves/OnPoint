from datetime import datetime, timedelta
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

from Schedules import Schedules
from Employee import Employee
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
        employee = Employee(**self.json_manager('employee', employee_id))
        schedule = employee.get_schedules()
        high_limit = schedule.time_in - timedelta(minutes=15)
        low_limit = schedule.time_in + timedelta(minutes=15)

        # Validando Entrada
        match state:
            # Fora de serviço -> Trabalhando
            case State.OUT_WORK:
                # Verifica se está entrando no horário certo
                #TODO Falta completar o "else"

                # adiciona o tempo atual na lista de clock ins
                schedule.append_clock_ins(now)
                if now <= high_limit or now >= low_limit:
                    
                    return True
                else:
                    raise ValueError("Entrando fora do horário proposto!")
            # Trabalhando -> Fora de serviço
            case State.WORKING:
                # adiciona o tempo atual na lista de clock outs
                schedule.append_clock_outs(now)
                if self.lunch_complete:
                    if now == self.entrance_time + schedule.hourly_time + schedule.lunch_time:
                        self.entrance_time = 0
                        self.lunch_start = 0
                        self.lunch_complete = False
                        return True
                    elif now > self.entrance_time + schedule.hourly_time + schedule.lunch_time:
                        raise ValueError("Saindo mais tarde")
                    else:
                        raise ValueError("Saindo mais cedo")
                else:
                    raise ValueError("Num almoçou pq?")
            case _:
                raise ValueError("Estado errado lek")

    def action_lunch(self, schedules: Schedules, state: State):

        # Validando
        match state:
            # Trabalhando -> Almoçando
            case State.WORKING:
                if self.lunch_start == 0:
                    if not self.lunch_complete:
                        self.lunch_start = datetime.now()
                        state = State.LUNCH
                        return True
                    else:
                        raise ValueError("Hora de almoço já foi completa")
                else:
                    raise ValueError("Horaário de almoço já foi iniciado")
            # Almoçando -> Trabalhando 
            case State.LUNCH:
                # Não sei se isso está certo
                if datetime.now() - self.lunch_start == schedules.lunch_time:
                    self.lunch_complete = True
                    state = State.WORKING
                    return True
                else:
                    raise ("Hora de almoço incompleto")
            case _ :
                raise ValueError("Estado errado")

    def justified_clock(self):
        pass
