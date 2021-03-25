# Generated by Django 3.1.7 on 2021-03-22 15:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 22, 15, 39, 12, 145515, tzinfo=utc)),
        ),
        migrations.AlterModelTable(
            name='realtor',
            table='realtors',
        ),
    ]