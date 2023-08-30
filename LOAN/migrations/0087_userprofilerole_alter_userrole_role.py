# Generated by Django 4.1 on 2023-05-06 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("LOAN", "0086_alter_center_center_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="userProfileRole",
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
                ("profileRoleName", models.CharField(max_length=100)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.CharField(max_length=100)),
                ("updated_date", models.DateTimeField(auto_now_add=True)),
                ("updated_by", models.CharField(max_length=100)),
                ("Charfield10", models.CharField(max_length=50, null=True)),
                ("Charfield20", models.CharField(max_length=50, null=True)),
                ("Charfield30", models.CharField(max_length=50, null=True)),
                ("Charfield40", models.CharField(max_length=50, null=True)),
                ("Charfield50", models.CharField(max_length=50, null=True)),
                ("Charfield60", models.CharField(max_length=50, null=True)),
                ("Charfield70", models.CharField(max_length=50, null=True)),
                ("Charfield80", models.CharField(max_length=50, null=True)),
                ("Charfield90", models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="userrole",
            name="role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="LOAN.userprofilerole"
            ),
        ),
    ]
