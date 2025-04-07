# Generated by Django 5.2 on 2025-04-07 06:01

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SavedBookmarks",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=core.utils.generate_id,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("url", models.URLField()),
                ("description", models.CharField(max_length=255)),
                ("source", models.CharField(max_length=100)),
                ("is_broken", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
