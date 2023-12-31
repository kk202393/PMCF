# Generated by Django 4.1 on 2022-11-12 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0027_customerkyc_updateddate_alter_customerkyc_timestamp"),
    ]

    operations = [
        migrations.AddField(
            model_name="approved_customer_kyc",
            name="updatedDate",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="disbursement_customer_kyc",
            name="updatedDate",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="rejected_customer_kyc",
            name="updatedDate",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="approved_customer_kyc",
            name="Timestamp",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="disbursement_customer_kyc",
            name="Timestamp",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="rejected_customer_kyc",
            name="Timestamp",
            field=models.DateTimeField(),
        ),
    ]
