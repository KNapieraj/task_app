# Generated by Django 4.2.1 on 2023-05-18 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zadanie_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='task',
            name='scheduled_date',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Date'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Complete', 'Complete'), ('Incomplete', 'Incomplete')], default='Incomplete', max_length=200),
        ),
    ]
