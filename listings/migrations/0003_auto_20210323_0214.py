# Generated by Django 3.1.7 on 2021-03-23 02:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210322_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 3, 23, 2, 14, 47, 133124, tzinfo=utc)),
        ),
    ]
