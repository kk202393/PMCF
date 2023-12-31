# Generated by Django 4.1 on 2022-11-20 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0035_remove_loanemi_intfield2_loanemi_emipaymentmode"),
    ]

    operations = [
        migrations.RenameField(
            model_name="loanemi",
            old_name="PaymentData",
            new_name="PaymentDate",
        ),
        migrations.CreateModel(
            name="auditTable",
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
                ("TransactionId", models.IntegerField()),
                ("emiReverseBy", models.CharField(max_length=50)),
                ("EmiReverseDate", models.DateTimeField()),
                ("EmiInstallmentDate", models.DateTimeField()),
                ("Charfield2", models.CharField(max_length=50, null=True)),
                ("Charfield3", models.CharField(max_length=50, null=True)),
                ("Charfield4", models.CharField(max_length=50, null=True)),
                ("Charfield5", models.CharField(max_length=50, null=True)),
                (
                    "loanId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="LOAN.loan_application_details",
                    ),
                ),
            ],
        ),
    ]
