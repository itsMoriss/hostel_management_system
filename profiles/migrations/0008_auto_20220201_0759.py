# Generated by Django 3.2.7 on 2022-02-01 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_profile_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='branch',
            new_name='hostel',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='state',
            new_name='room_number',
        ),
    ]
