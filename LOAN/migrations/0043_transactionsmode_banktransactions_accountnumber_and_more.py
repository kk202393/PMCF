# Generated by Django 4.1 on 2022-11-29 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0042_banktransactions"),
    ]

    operations = [
        migrations.CreateModel(
            name="TransactionsMode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("TransactionsValue", models.CharField(max_length=50, null=True)),
                ("CreatedBy", models.CharField(max_length=50, null=True)),
                ("UpdatedBy", models.CharField(max_length=50, null=True)),
                ("CreatedDate", models.DateTimeField(null=True)),
                ("UpadtedDate", models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name="banktransactions",
            name="AccountNumber",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="banktransactions",
            name="BankName",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="LOAN.bankname",
            ),
        ),
        migrations.AddField(
            model_name="banktransactions",
            name="Center",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, to="LOAN.center"
            ),
        ),
        migrations.AddField(
            model_name="banktransactions",
            name="Remarks",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="banktransactions",
            name="TransactionsAmount",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="banktransactions",
            name="TransactionsDate",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="banktransactions",
            name="TransactionsSlipNumber",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="banktransactions",
            name="TransactionsMode",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="LOAN.transactionsmode",
            ),
        ),
    ]