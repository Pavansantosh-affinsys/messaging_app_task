from twilio.rest import Client
from message_queue import settings
from django.core.mail import send_mail


def message_sms_account_created(instance):
    client = Client(settings.account_sid, settings.auth_token)
    message = client.messages.create(
        body=f"\nHello {instance.firstname},\nThankyou for creating an account in BankBuddy",
        from_=f"{settings.mobile_number}",
        to=f"+91{instance.mobile_number}",
    )


def email_account_created(instance):
    subject = "Welcome to the family"
    message = (
        f"Hello {instance.firstname},\nThankyou for creating an account in BankBuddy"
    )
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [instance.email])


def message_sms_transaction_debit(key, amount, account_holder):
    payee = account_holder.objects.get(pk=key)
    client = Client(settings.account_sid, settings.auth_token)
    message = client.messages.create(
        body=f"""Hello {payee.firstname},
                 Your account got debited by Rs.{amount}.Your present balance is Rs.{payee.account_balance}""",
        from_=f"{settings.mobile_number}",
        to=f"+91{payee.mobile_number}",
    )


def message_sms_transaction_credit(key, amount, account_holder):
    beneficiary = account_holder.objects.get(pk=key)
    client = Client(settings.account_sid, settings.auth_token)
    message = client.messages.create(
        body=f"""Hello {beneficiary.firstname},
                 Your account got debited by Rs.{amount}.Your present balance is Rs.{beneficiary.account_balance}""",
        from_=f"{settings.mobile_number}",
        to=f"+91{beneficiary.mobile_number}",
    )


def email_account_transaction_debit(key, amount, account_holder):
    payee = account_holder.objects.get(pk=key)
    subject = "Transaction History"
    message = f"""Hello {payee.firstname},
                  Your account got debited by Rs.{amount}.Your present balance is Rs.{payee.account_balance}"""
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [payee.email])


def email_account_transaction_credit(key, amount, account_holder):
    beneficiary = account_holder.objects.get(pk=key)
    subject = "Transaction History"
    message = f"""Hello {beneficiary.firstname},
                  Your account got credited by Rs.{amount}.Your present balance is Rs.{beneficiary.account_balance}"""
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [beneficiary.email])


def sufficient_amount(key, amount, account_holder):
    amount_present = account_holder.objects.get(pk=key)
    if amount_present.account_balance < amount:
        return False
    return True
