# Generated by Django 4.1 on 2023-04-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0063_remove_loandetails_intfield1_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="center",
            name="Charfield1",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="center",
            name="Charfield2",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="center",
            name="Charfield3",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="center",
            name="Charfield4",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="center",
            name="Charfield5",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="center",
            name="Charfield6",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="center",
            name="Charfield7",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="center",
            name="Charfield8",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="center",
            name="Charfield9",
            field=models.CharField(max_length=50, null=True),
        ),
    ]