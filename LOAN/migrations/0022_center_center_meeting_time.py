# Generated by Django 4.1 on 2022-11-02 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0021_alter_disbursement_customer_kyc_customeremi_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="center",
            name="center_meeting_time",
            field=models.TimeField(null=True),
        ),
    ]
