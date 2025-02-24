from datetime import datetime, timedelta

import Schedules
from ..utils import State

class Clock():
    def __init__(self):
        self.entrance_time: datetime = datetime()
        self.lunch_complete: bool = False
        self.lunch_start: datetime = datetime()

    def validate_clock(self, schedules: Schedules, state: State):
        now = datetime.now()
        high_limit = schedules.time_in - timedelta(minutes=15)
        low_limit = schedules.time_in + timedelta(minutes=15)
        
        match state:
            # Fora de serviço -> Trabalhando
            case State.OUT_WORK:
                # Verifica se está entrando no horário certo
                #TODO Falta completar o "else"
                if now <= high_limit or now >= low_limit:
                    return True
            # Trabalhando -> Fora de serviço
            case State.WORKING:
                if self.lunch_complete:
                    if now == self.entrance_time + schedules.hourly_time + schedules.lunch_time:
                        self.entrance_time = 0
                        self.lunch_start = 0
                        self.lunch_complete = False
                        return True
                    elif now > self.entrance_time + schedules.hourly_time + schedules.lunch_time:
                        raise ValueError("Saindo mais tarde")
                    else:
                        raise ValueError("Saindo mais cedo")
            case _:
                raise ValueError("Estado errado lek")

    def validate_lunch(self, schedules: Schedules, state: State):

        match state:
            # Trabalhando -> Almoçando
            case State.WORKING:
                if self.lunch_start == 0:
                    if not self.lunch_complete:
                        self.lunch_start = datetime.now()
                        state = State.LUNCH
                        return True
            # Almoçando -> Trabalhando 
            case State.LUNCH:
                #if datetime.now() - self.lunch_start == schedules.lunch_time:
                self.lunch_complete = True
                state = State.WORKING
                return True
            case _ :
                raise ValueError("Ta errado aí lek")
                    

        
    def action_clock(self, schedules: Schedules, state: State):
        self.validade_clock(schedules=schedules, state=state)
        #self.entranceTime = datetime.now()

    def action_lunch(self, schedules: Schedules, state: State):
        self.validate_lunch(schedules=schedules, state=state)

    def justified_clock(self):
        pass
