# Generated by Django 2.0.3 on 2018-03-30 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 30, 17, 19, 49, 958076), verbose_name='时间'),
        ),
    ]