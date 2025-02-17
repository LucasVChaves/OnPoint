from datetime import datetime

class User:
    def __init__(self, user: str, pin: int, name: str, email: str, birth: datetime):
        self.user = user
        self.pin = pin
        self.name = name
        self.email = email
        self.birth: datetime = birth

    def get_user(self) -> str:
        return self.user

    def get_pin(self) -> int:
        return self.pin

    def get_name(self) -> str:
        return self.name

    def get_email(self) -> str:
        return self.email

    def set_user(self, user: str):
        self.user = user

    def set_pin(self, pin: int):
        self.pin = pin

    def set_name(self, name: str):
        self.name = name

    def set_email(self, email: str):
        self.email = email