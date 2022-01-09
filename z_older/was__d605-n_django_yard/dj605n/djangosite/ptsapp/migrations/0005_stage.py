# Generated by Django 3.2 on 2021-09-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptsapp', '0004_auto_20210929_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_identification', models.CharField(blank=True, default='', max_length=252)),
                ('source', models.CharField(blank=True, default='', max_length=252)),
                ('topology', models.CharField(blank=True, default='', max_length=252)),
                ('center_distance_mm', models.IntegerField(blank=True, null=True)),
                ('module_mm', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('helix_angle_deg', models.IntegerField(blank=True, null=True)),
                ('reduction_ratio', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('input_shaft_bearing_configuration', models.CharField(blank=True, max_length=252, null=True)),
                ('output_shaft_bearing_configuration', models.CharField(blank=True, max_length=252, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('active_status', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]