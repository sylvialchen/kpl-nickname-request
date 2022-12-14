# Generated by Django 4.1.2 on 2022-10-21 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0006_alter_sister_crossing_year_alter_sister_line_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nickname_request",
            name="name",
            field=models.CharField(max_length=20, verbose_name="nickname request"),
        ),
        migrations.AlterField(
            model_name="sister",
            name="big_sister",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="main_app.sister",
            ),
        ),
    ]
