# Generated by Django 4.1.2 on 2022-10-21 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0002_alter_sister_line_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sister",
            name="crossing_number",
        ),
        migrations.AddField(
            model_name="sister",
            name="crossing_year",
            field=models.PositiveSmallIntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sister",
            name="nickname_meaning",
            field=models.TextField(
                default=0.0004945598417408506, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sister",
            name="line_number",
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.CreateModel(
            name="PNM",
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
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=25)),
                ("chapter", models.CharField(default="null", max_length=10)),
                ("process_chapter", models.CharField(
                    default="null", max_length=10)),
                ("process_semester", models.CharField(max_length=6)),
                ("process_year", models.PositiveSmallIntegerField()),
                ("potential_line_number", models.PositiveSmallIntegerField()),
                (
                    "big_sister",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main_app.sister",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Nickname_Request",
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
                ("name", models.CharField(max_length=20)),
                ("nickname_meaning", models.TextField(max_length=250)),
                ("req_date", models.DateTimeField(verbose_name="date requested")),
                (
                    "pnm",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main_app.pnm",
                    ),
                ),
            ],
        ),
    ]