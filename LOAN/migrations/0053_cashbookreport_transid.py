# Generated by Django 4.1 on 2023-01-04 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0052_account_transections_charfield2_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cashbookreport",
            name="TransID",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="LOAN.account_transections",
            ),
        ),
    ]
