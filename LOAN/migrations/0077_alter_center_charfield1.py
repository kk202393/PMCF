# Generated by Django 4.1 on 2023-05-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0076_alter_center_center_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="center",
            name="Charfield1",
            field=models.DateField(),
        ),
    ]
