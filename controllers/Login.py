import json
import datetime
import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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

    def forgotPIN(self, user):
        user_record = None
        if self.userdb == "Employee":
            user_record = Empployee.query.filter_by(user=user).first()
        elif self.userdb == "Admin":
            user_record = Admin.query.filter_by(user=user).first()

        if user_record:
            new_pin = ''.join(random.choices(string.digits, k=8))
            user_record.PIN = new_pin
            self.userdb.session.commit()

            msg = MIMEMultipart()
            msg['From'] = 'noreply@gmail.com'
            msg['To'] = user_record.email
            msg['Subject'] = 'Your new PIN'

            body = f'Hello {user},\n\nYour new PIN is: {new_pin}\n\nBest regards,\nOn Point Team'
            msg.attach(MIMEText(body, 'plain'))

            try:  # manda email,precisa de um email e senha para funcionar******
                server = smtplib.SMTP('smtp.example.com', 587)
                server.starttls()
                server.login('your_email@example.com', 'your_password')
                text = msg.as_string()
                server.sendmail('your_email@example.com', user_record.email, text)
                server.quit()
                print("Email sent successfully")
            except Exception as e:
                print(f"Failed to send email: {e}")
        else:
            print("User not found")
        pass