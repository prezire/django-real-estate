# Generated by Django 3.1.7 on 2021-03-23 02:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20210323_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y%m%dH%M%S'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y%m%dH%M%S'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%Y%m%dH%M%S'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%Y%m%dH%M%S'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='photos/%Y%m%dH%M%S'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/%Y%m%dH%M%S'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 3, 23, 2, 44, 2, 943225, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='ListingPhoto',
        ),
    ]
