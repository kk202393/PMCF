# Generated by Django 4.1 on 2022-11-01 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0018_remove_disbursement_customer_kyc_customeremi"),
    ]

    operations = [
        migrations.AddField(
            model_name="disbursement_customer_kyc",
            name="CustomerEMI",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.PROTECT,
                to="LOAN.loanemi",
            ),
        ),
    ]
