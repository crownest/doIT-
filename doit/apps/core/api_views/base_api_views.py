# Third-Party
from rest_framework import viewsets, mixins
from djoser.views import LoginView as _LoginView

# Local Django
from users.models import User
from core.models import Contact
from doit.modules import MailModule
from core.serializers import (
    LoginSerializer, ContactSerializer, ContactCreateSerializer
)


class LoginView(_LoginView):
    serializer_class = LoginSerializer

    def _action(self, serializer):
        action = super(LoginView, self)._action(serializer)

        action.data.update({
            'user_id': serializer.user.id,
        })

        return action


class ContactViewSet(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Contact.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ContactCreateSerializer
        else:
            return ContactSerializer

    def get_permissions(self):
        permissions = super(ContactViewSet, self).get_permissions()

        if self.action == 'create':
            return []

        return permissions

    def perform_create(self, serializer):
        contact = serializer.save()

        # Send Contact Mail
        users = User.objects.filter(is_superuser=True)
        for user in users:
            MailModule.send_contact_mail(contact, user)
