# Generated by Django 4.1 on 2022-12-25 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0045_remove_cashbookreport_branch_cashbookreport_center"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cashbookreport",
            name="Center",
        ),
        migrations.AddField(
            model_name="cashbookreport",
            name="Branch",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, to="LOAN.branch"
            ),
        ),
    ]
