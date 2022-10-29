from django.db import models
from django.db.models import signals, F
from django.dispatch import receiver
from datetime import datetime
from .utility import message_sms, email


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
def message_on_create(sender, instance, created, *args, **kwargs):
    if created:
        email(instance)
        message_sms(instance)


class TransactionsDetails(models.Model):
    beneficiary_ID = models.ForeignKey(
        AccountHolder, on_delete=models.CASCADE, related_name="credit"
    )
    payee_ID = models.ForeignKey(
        AccountHolder, on_delete=models.CASCADE, related_name="debit"
    )
    amount = models.PositiveIntegerField(null=False, blank=False)
    transaction_date = models.DateTimeField(
        "Created Time", auto_now_add=True, null=True
    )


@receiver(signals.pre_save, sender=TransactionsDetails)
def update_account_table(sender, instance, **kwargs):
    AccountHolder.objects.filter(pk=instance.beneficiary_ID).update(
        account_balance=F("account_balance") + instance.amount
    )
    AccountHolder.objects.filter(pk=instance.payee_ID).update(
        account_balance=F("account_balance") + instance.amount
    )


class Recommendations(models.Model):
    time = models.DateTimeField()
    description = models.TextField(max_length=100)
