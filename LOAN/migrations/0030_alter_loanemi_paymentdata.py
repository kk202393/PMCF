# Generated by Django 4.1 on 2022-11-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0029_emicount_remove_loanemi_datefield1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loanemi",
            name="PaymentData",
            field=models.DateTimeField(null=True),
        ),
    ]
