from django.db import models


class AccountHolder(models.Model):
    firstname = models.CharField(max_length=20, null=False)
    lastname = models.CharField(max_length=20, null=False, blank=True)
    mobile_number = models.PositiveIntegerField(max_length=10, null=False)
    email = models.EmailField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    account_balance = models.PositiveIntegerField(null=False, default=0)

