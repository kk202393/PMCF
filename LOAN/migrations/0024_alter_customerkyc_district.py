# Generated by Django 4.1 on 2022-11-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0023_loanemi_loanmode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerkyc",
            name="District",
            field=models.CharField(max_length=100),
        ),
    ]