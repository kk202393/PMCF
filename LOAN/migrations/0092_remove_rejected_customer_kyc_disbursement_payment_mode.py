# Generated by Django 4.1 on 2023-05-08 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0091_userrole"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rejected_customer_kyc",
            name="Disbursement_Payment_Mode",
        ),
    ]