# Generated by Django 4.1.2 on 2022-10-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MailService", "0004_alter_accountholder_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="transactionsdetails",
            name="transaction_date",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Created Time"
            ),
        ),
    ]
