# Generated by Django 4.1 on 2022-11-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0033_alter_loanemi_transactionid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="loanemi",
            name="Doc2image",
        ),
        migrations.AddField(
            model_name="loanemi",
            name="emiSubmittedBy",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
