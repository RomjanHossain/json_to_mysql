# Generated by Django 4.1.3 on 2022-11-30 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jsonapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jsonmodel",
            name="sajdah_number",
            field=models.IntegerField(null=True),
        ),
    ]
