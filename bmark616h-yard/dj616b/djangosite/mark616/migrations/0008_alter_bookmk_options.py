# Generated by Django 3.2 on 2022-01-22 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mark616', '0007_rename_is_shaarli_bookmk_id_shaarli'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmk',
            options={'ordering': ('-created_at',)},
        ),
    ]
