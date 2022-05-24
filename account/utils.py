ACCOUNT_TYPE = [
        ('SUPER_USER', 'SUPER_USER'),
        ('ADMIN', 'ADMIN'),        
        ('TSP', 'TSP'),
        ('USER', 'USER'),
    ]

ADMIN = 'ADMIN'
TSP = 'TSP'
USER = 'USER'
SUPER_USER = 'SUPER_USER'


from django.core.mail import EmailMessage
import os

class Util:
    @staticmethod
    def send_email(data):
        email=EmailMessage(subject=data['subject'],body=data['body'],from_email=os.environ.get('EMAIL_FORM'),to=[data['to_email']])
        email.send()
        
#from_email=os.environ.get('EMAIL_FORM')
#from_email='sachinwb1991@gmail.com'