# Generated by Django 4.1.2 on 2022-10-21 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sister",
            name="line_number",
            field=models.IntegerField(max_length=3),
        ),
    ]
