# Generated by Django 4.1 on 2023-02-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0055_rename__100note_cashbookreport_coin1_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customerkyc",
            name="Charfield10",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="customerkyc",
            name="Charfield6",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="customerkyc",
            name="Charfield7",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="customerkyc",
            name="Charfield8",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="customerkyc",
            name="Charfield9",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="customerkyc",
            name="Custimage",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
