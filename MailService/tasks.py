from django.core.mail import send_mail
from message_queue import settings

from message_queue.celery import app


@app.task(bind=True)
def email_recommendations(self, emails, description):
    subject = "Recommendations"
    message = f"{description}"
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, emails)
