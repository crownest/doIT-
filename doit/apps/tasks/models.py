# Django
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.utils.translation import ugettext_lazy as _


class Task(models.Model):
        title = models.CharField(
            verbose_name=_('Title'), max_length=1000, blank=True
        )
        description = models.TextField(
            verbose_name=_('Description'), max_length=10000, null=True
        )
        user = models.ForeignKey(
            verbose_name=_('User'), to='users.User', related_name='tasks'
        )

        class Meta:
            ordering = ('id',)

        def __str__(self):
            return '{title}'.format(title=self.title)


class Reminder(models.Model):
        task = models.ForeignKey(
            verbose_name=_('Task'), to='tasks.Task', related_name='reminders'
        )
        date = models.DateTimeField(
            verbose_name=_('Date'), blank=True, null=True,
        )

        class Meta:
            ordering = ('date',)

        def __str__(self):
            return '{task} - {date}'.format(
	            task=self.task.title, date=self.date
            )
