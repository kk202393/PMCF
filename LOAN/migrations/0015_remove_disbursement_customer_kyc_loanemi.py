# Generated by Django 4.1 on 2022-10-28 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0014_alter_haed_office_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="disbursement_customer_kyc",
            name="loanEMI",
        ),
    ]
