import datetime
from django.db import models
from django.db.models import signals, F
from django.dispatch import receiver
from .utility import (
    message_sms_account_created,
    email_account_created,
    sufficient_amount,
    message_sms_transaction_debit,
    email_account_transaction_debit,
    message_sms_transaction_credit,
    email_account_transaction_credit,
)
from django.core.exceptions import ValidationError
from .tasks import email_recommendations
from django.utils import timezone


class AccountHolder(models.Model):
    firstname = models.CharField(max_length=20, null=False, blank=False)
    lastname = models.CharField(max_length=20, null=False, blank=True)
    mobile_number = models.IntegerField(
        max_length=10, null=False, blank=False, unique=True
    )
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    account_balance = models.PositiveIntegerField(null=False, default=0)


@receiver(signals.post_save, sender=AccountHolder)
def communication(sender, instance, created, *args, **kwargs):
    if created:
        email_account_created(instance)
        message_sms_account_created(instance)


class TransactionsDetails(models.Model):
    payee_ID = models.ForeignKey(
        AccountHolder, on_delete=models.CASCADE, related_name="debit"
    )
    beneficiary_ID = models.ForeignKey(
        AccountHolder, on_delete=models.CASCADE, related_name="credit"
    )
    amount = models.PositiveIntegerField(null=False, blank=False)
    transaction_date = models.DateTimeField(
        "Created Time", auto_now_add=True, null=True
    )


@receiver(signals.pre_save, sender=TransactionsDetails)
def update_account_table(sender, instance, **kwargs):
    if not sufficient_amount(instance.payee_ID.id, instance.amount, AccountHolder):
        raise ValidationError("insufficient balance")
    AccountHolder.objects.filter(pk=instance.payee_ID.id).update(
        account_balance=F("account_balance") - instance.amount
    )
    AccountHolder.objects.filter(pk=instance.beneficiary_ID.id).update(
        account_balance=F("account_balance") + instance.amount
    )


@receiver(signals.post_save, sender=TransactionsDetails)
def inform(sender, instance, created, *args, **kwargs):
    if created:
        email_account_transaction_debit(
            instance.payee_ID.id, instance.amount, AccountHolder
        )
        email_account_transaction_credit(
            instance.beneficiary_ID.id, instance.amount, AccountHolder
        )
        message_sms_transaction_debit(
            instance.payee_ID.id, instance.amount, AccountHolder
        )
        message_sms_transaction_credit(
            instance.beneficiary_ID.id, instance.amount, AccountHolder
        )


class Recommendations(models.Model):
    time = models.DateTimeField(blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)


@receiver(signals.post_save, sender=Recommendations)
def schedule_task(sender, instance, created, *args, **kwargs):
    emails = list(AccountHolder.objects.all().values_list("email", flat=True))
    if created:
        email_recommendations.apply_async(
            args=(emails, instance.description), eta=instance.time
        )
