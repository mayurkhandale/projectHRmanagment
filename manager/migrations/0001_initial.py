# Generated by Django 3.0.2 on 2020-02-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New_reqModel',
            fields=[
                ('opprtunity_code', models.IntegerField(primary_key=True, serialize=False)),
                ('qualifucation', models.CharField(max_length=30)),
                ('registratin_start_from', models.DateField()),
                ('age_limit', models.IntegerField()),
                ('last_day_apply', models.DateField()),
                ('department_id', models.CharField(max_length=30)),
                ('no_of_position', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('resposibility', models.CharField(max_length=100)),
                ('contact_no', models.IntegerField(max_length=10)),
            ],
        ),
    ]
