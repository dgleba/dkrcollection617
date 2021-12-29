# Generated by Django 3.2 on 2021-09-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptsapp', '0002_auto_20210827_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='vehicles',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='applications',
            field=models.ManyToManyField(to='ptsapp.Application'),
        ),
    ]
