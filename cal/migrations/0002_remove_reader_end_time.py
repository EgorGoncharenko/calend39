# Generated by Django 3.0.7 on 2020-07-02 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='end_time',
        ),
    ]
