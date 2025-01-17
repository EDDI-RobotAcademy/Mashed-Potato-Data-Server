# Generated by Django 5.1.3 on 2025-01-06 06:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=32)),
            ],
            options={
                "db_table": "car",
            },
        ),
        migrations.CreateModel(
            name="CarDescription",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("description", models.TextField()),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="descriptions",
                        to="car.car",
                    ),
                ),
            ],
            options={
                "db_table": "car_description",
            },
        ),
        migrations.CreateModel(
            name="CarImage",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("image", models.CharField(max_length=100, null=True)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="car.car",
                    ),
                ),
            ],
            options={
                "db_table": "car_image",
            },
        ),
        migrations.CreateModel(
            name="CarPrice",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("price", models.IntegerField()),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prices",
                        to="car.car",
                    ),
                ),
            ],
            options={
                "db_table": "car_price",
            },
        ),
    ]
