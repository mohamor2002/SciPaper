# Generated by Django 4.2.7 on 2023-12-30 20:11

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="paper",
            fields=[
                (
                    "titre",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="titre"
                    ),
                ),
                (
                    "p_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("resume", models.TextField(blank=True, verbose_name="resume")),
                (
                    "auteurs",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True, max_length=100, null=True
                        ),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "mots_cles",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True, max_length=100, null=True
                        ),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "institutions",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True, max_length=100, null=True
                        ),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "texte_integral",
                    models.TextField(
                        blank=True, null=True, verbose_name="text integral"
                    ),
                ),
                (
                    "file_pdf",
                    models.FileField(
                        blank=True,
                        max_length=40000,
                        null=True,
                        upload_to="uploads/",
                        verbose_name="file pdf",
                    ),
                ),
                (
                    "references",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True, max_length=50, null=True
                        ),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                ("date_insertion", models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                "verbose_name": "paper",
                "verbose_name_plural": "papers",
                "get_latest_by": "date_insertion",
                "default_related_name": "paper",
            },
        ),
    ]
