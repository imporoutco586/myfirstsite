# Generated by Django 4.2.1 on 2023-07-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myfrtsite", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserInfo",
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
                ("username", models.CharField(max_length=40)),
                ("phoneNum", models.CharField(max_length=11)),
                ("password", models.CharField(max_length=40)),
            ],
        ),
    ]
