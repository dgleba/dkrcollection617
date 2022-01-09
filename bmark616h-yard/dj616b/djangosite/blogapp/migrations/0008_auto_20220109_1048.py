# Generated by Django 3.2 on 2022-01-09 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20211222_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.RemoveField(
            model_name='vehicle2',
            name='application2s',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-id',)},
        ),
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.DeleteModel(
            name='Application2',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
        migrations.DeleteModel(
            name='Vehicle2',
        ),
    ]