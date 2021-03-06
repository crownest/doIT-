# Standart Library
import datetime

# Third-Party
from rest_framework import serializers

# Django
from django.utils.translation import ugettext_lazy as _

# Local Django
from tasks.models import Task, Reminder


class ReminderSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(error_messages={
        'invalid': _('Datetime has wrong format.')
    })

    class Meta:
        model = Reminder
        fields = ('id', 'task', 'date', 'locale_date', 'is_completed')

    def validate_task(self, value):
        user = self.context['request'].user

        if user != value.user:
            raise serializers.ValidationError(_('Not found.'))

        return value

    def validate_date(self, value):
        if value <= datetime.datetime.utcnow():
            raise serializers.ValidationError(_('Can not add past reminder.'))

        return value


class ReminderListSerializer(ReminderSerializer):
    pass


class ReminderCreateSerializer(ReminderSerializer):

    class Meta:
        model = Reminder
        fields = ('id', 'task', 'date', 'locale_date', 'is_completed')


class ReminderRetrieveSerializer(ReminderSerializer):
    pass


class ReminderUpdateSerializer(ReminderSerializer):

    class Meta:
        model = Reminder
        fields = ('id', 'date', 'locale_date', 'is_completed')

    def validate_date(self, value):
        super(ReminderUpdateSerializer, self).validate_date(value)

        if value == self.instance.date:
            raise serializers.ValidationError(_('Can not select same reminder.'))

        return value


class TaskSerializer(serializers.ModelSerializer):
    reminders = ReminderSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'status', 'reminders')


class TaskListSerializer(TaskSerializer):

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'status')


class TaskCreateSerializer(TaskSerializer):
    reminders = ReminderCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'reminders')


class TaskRetrieveSerializer(TaskSerializer):
    reminders = ReminderRetrieveSerializer(many=True, read_only=True)


class TaskUpdateSerializer(TaskSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description')
