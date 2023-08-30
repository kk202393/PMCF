# Generated by Django 4.1 on 2022-10-28 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0013_alter_loanemi_emistatus"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="haed_office",
            options={"verbose_name_plural": "1. head_office"},
        ),
        migrations.AddField(
            model_name="disbursement_customer_kyc",
            name="loanEMI",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="LOAN.loanemi",
            ),
            preserve_default=False,
        ),
    ]