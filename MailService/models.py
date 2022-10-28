from django.db import models


class AccountHolder(models.Model):
    firstname = models.CharField(max_length=20, null=False, blank=False)
    lastname = models.CharField(max_length=20, null=False, blank=True)
    mobile_number = models.IntegerField(max_length=10, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    account_balance = models.PositiveIntegerField(null=False, default=0)


class TransactionsDetails(models.Model):
    beneficiary_ID = models.ForeignKey(AccountHolder, on_delete=models.CASCADE, related_name='credit')
    payee_ID = models.ForeignKey(AccountHolder, on_delete=models.CASCADE, related_name='debit')
    amount = models.PositiveIntegerField(null=False, blank=False)


class Recommendations(models.Model):
    time = models.DateTimeField()
    description = models.TextField(max_length=100)
