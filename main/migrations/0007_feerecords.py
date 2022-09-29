# Generated by Django 3.2.7 on 2022-02-01 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_feepaid'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=20, null=True)),
                ('student_name', models.CharField(blank=True, max_length=50, null=True)),
                ('college', models.CharField(blank=True, max_length=100, null=True)),
                ('amount_paid', models.CharField(blank=True, max_length=100, null=True)),
                ('balance', models.CharField(blank=True, max_length=10, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'FeesRecords',
                'ordering': ['-date_created'],
            },
        ),
    ]
