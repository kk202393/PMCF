# Generated by Django 4.1 on 2022-10-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0011_emistatus_loanemi"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loanemi",
            name="installmentDate",
            field=models.DateTimeField(),
        ),
    ]