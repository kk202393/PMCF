# Generated by Django 4.1 on 2023-05-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0097_alter_account_transaction_transdate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="loandetails",
            name="intfield3",
        ),
        migrations.AddField(
            model_name="loandetails",
            name="activateStatus",
            field=models.BooleanField(null=True),
        ),
    ]