# Generated by Django 4.1.2 on 2022-10-29 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("MailService", "0005_transactionsdetails_transaction_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="transactionsdetails",
            options={
                "ordering": ["payee_ID", "beneficiary_ID", "amount", "transaction_date"]
            },
        ),
    ]
