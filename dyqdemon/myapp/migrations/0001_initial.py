# Generated by Django 2.2.24 on 2021-09-27 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField(default=20)),
                ('phone', models.CharField(max_length=16)),
                ('create_time', models.DateTimeField(default=datetime.datetime(2021, 9, 27, 18, 44, 34, 423451))),
            ],
        ),
    ]