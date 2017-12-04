# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-04 17:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_reminder_celery_task_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reminder',
            options={'ordering': ('task', 'date'), 'verbose_name': 'Reminder', 'verbose_name_plural': 'Reminders'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('user', '-id'), 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
    ]
