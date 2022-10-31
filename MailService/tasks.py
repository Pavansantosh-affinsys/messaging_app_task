import requests
from django.core.mail import send_mail
from message_queue import settings
from message_queue.celery import app
from celery import shared_task


account_url = "http://127.0.0.1:8000/api/account/"


@app.task(bind=True)
def email_recommendations(self, emails, description):
    subject = "Recommendations"
    message = f"{description}"
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, emails)


@shared_task(bind=True)
def scheduled_task(self):
    subject = "Scheduled task"
    message = "this is a dummy text email"
    email_from = settings.EMAIL_HOST_USER
    account_details = requests.get(account_url).json()
    emails = [i["email"] for i in account_details]
    send_mail(subject, message, email_from, emails)

