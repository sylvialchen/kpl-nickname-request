# Generated by Django 4.1.2 on 2022-10-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0008_alter_sister_little_sister_crossed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sister",
            name="crossing_year",
            field=models.IntegerField(),
        ),
    ]