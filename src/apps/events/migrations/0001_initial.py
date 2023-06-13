# Generated by Django 4.2.2 on 2023-06-12 17:39

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("start", models.DateTimeField()),
                ("end", models.DateTimeField()),
                ("description", models.TextField(blank=True)),
                ("meeting_link", models.URLField(blank=True, null=True)),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
    ]