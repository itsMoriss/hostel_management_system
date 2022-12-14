# Generated by Django 3.2.3 on 2021-11-08 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_visiting', models.CharField(blank=True, max_length=20, null=True)),
                ('departure_date', models.CharField(blank=True, max_length=20, null=True)),
                ('arrival_date', models.CharField(blank=True, max_length=20, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_leave_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Student Leave',
                'ordering': ['-date_created'],
            },
        ),
    ]
