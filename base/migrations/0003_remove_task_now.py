# Generated by Django 4.1.1 on 2022-09-15 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_task_now'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='now',
        ),
    ]