# Generated by Django 3.1.7 on 2021-04-02 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0013_auto_20210402_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intimemodel',
            name='City',
            field=models.CharField(default=False, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='DateOfJoin',
            field=models.DateField(default=datetime.datetime(2021, 4, 2, 10, 31, 52, 752056)),
        ),
    ]