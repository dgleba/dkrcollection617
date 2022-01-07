# Generated by Django 3.2 on 2021-10-20 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ptsapp', '0009_auto_20211020_0545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gear',
            old_name='cumulative_pitch_error_μm',
            new_name='cumulative_pitch_error_microm',
        ),
        migrations.RenameField(
            model_name='gear',
            old_name='internal_identification',
            new_name='gear_identification',
        ),
        migrations.RenameField(
            model_name='gear',
            old_name='helix_slope_deviation_μm',
            new_name='helix_slope_deviation_microm',
        ),
        migrations.RenameField(
            model_name='gear',
            old_name='profile_angle_deviation_μm',
            new_name='profile_angle_deviation_microm',
        ),
        migrations.RenameField(
            model_name='gear',
            old_name='profile_form_deviation_μm',
            new_name='profile_form_deviation_microm',
        ),
        migrations.RenameField(
            model_name='gear',
            old_name='total_composite_action_tolerance_μm',
            new_name='total_composite_action_tolerance_microm',
        ),
    ]
