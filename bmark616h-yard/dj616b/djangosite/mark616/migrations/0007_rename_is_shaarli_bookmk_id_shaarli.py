# Generated by Django 3.2 on 2022-01-21 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mark616', '0006_bookmk_is_shaarli'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmk',
            old_name='is_shaarli',
            new_name='id_shaarli',
        ),
    ]
