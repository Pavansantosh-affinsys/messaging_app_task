# Generated by Django 4.1.2 on 2022-10-28 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("MailService", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Recommendations",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField()),
                ("description", models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="TransactionsDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.PositiveIntegerField()),
                (
                    "beneficiary_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="credit",
                        to="MailService.accountholder",
                    ),
                ),
                (
                    "payee_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="debit",
                        to="MailService.accountholder",
                    ),
                ),
            ],
        ),
    ]
