# Generated by Django 4.1 on 2022-11-04 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0022_center_center_meeting_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="loanemi",
            name="loanMode",
            field=models.ForeignKey(
                default=7,
                on_delete=django.db.models.deletion.PROTECT,
                to="LOAN.loan_mode_data",
            ),
        ),
    ]
