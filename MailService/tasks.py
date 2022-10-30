from django.core.mail import send_mail
from message_queue import settings

from message_queue.celery import app
from time import sleep
from celery import shared_task


@app.task(bind=True)
def email_recommendations(self, emails, description):
    subject = "Recommendations"
    message = f"{description}"
    email_from = settings.EMAIL_HOST_USER
    # sleep(20)
    send_mail(subject, message, email_from, emails)
