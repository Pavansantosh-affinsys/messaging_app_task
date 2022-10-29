from twilio.rest import Client
from message_queue import settings
from django.core.mail import send_mail


def message_sms(instance):
    client = Client(settings.account_sid, settings.auth_token)
    message = client.messages.create(
        body=f'\nHello {instance.firstname},\nThankyou for creating an account in BankBuddy',
        from_=f'{settings.mobile_number}',
        to=f'+91{instance.mobile_number}'
    )
    print(message.sid)


def email(instance):
    subject = 'Welcome to the family'
    message = f'Hello {instance.firstname},\nThankyou for creating an account in BankBuddy'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [instance.email])

