# Generated by Django 4.1 on 2023-05-31 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0099_alter_loandetails_number_of_months"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loandetails",
            name="activateStatus",
            field=models.BooleanField(default=True),
        ),
    ]
