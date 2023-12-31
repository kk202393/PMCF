# Generated by Django 4.1 on 2023-05-07 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("LOAN", "0090_delete_userrole"),
    ]

    operations = [
        migrations.CreateModel(
            name="userRole",
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
                (
                    "branchName",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="LOAN.branch"
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="auth.group"
                    ),
                ),
                (
                    "userName",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="LOAN.userprofilerole",
                    ),
                ),
            ],
        ),
    ]
