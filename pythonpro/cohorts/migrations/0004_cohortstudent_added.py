# Generated by Django 2.0.6 on 2018-06-12 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0003_webinar'),
    ]

    operations = [
        migrations.AddField(
            model_name='cohortstudent',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 12, 0, 0)),
        ),
    ]
