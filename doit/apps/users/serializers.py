# Third-Party
from rest_framework import serializers

# Local Django
from users.models import User
from django.contrib.auth import password_validation


# Base

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'is_active', 'is_verified'
        )


class UserListSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class UserDetailSerializer(UserSerializer):
    pass


class UserCreateSerializer(UserSerializer):

    class Meta:
        model = User
        fields = (
            'email', 'first_name', 'last_name', 'password'
        )
        extra_kwargs = {'password': {'write_only': True}}


class UserUpdateSerializer(UserSerializer):

    class Meta:
        model = User
        fields = (
            'email', 'first_name', 'last_name'
        )


class UserPasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_new_password = serializers.CharField()

    class Meta:
        fields = (
            'old_password', 'new_password', 'confirm_new_password'
        )

    def validate_confirm_new_password(self, value):
        if self.initial_data['new_password'] != self.initial_data['confirm_new_password']:
            raise serializers.ValidationError(
                "The two password fields didn't match."
            )

        password_validation.validate_password(
            self.initial_data['confirm_new_password']
        )

        return value

    def validate_old_password(self, value):
        user = self.context['user']

        if not user.check_password(value):
            raise serializers.ValidationError(
                'Your old password was entered incorrectly. '
                'Please enter it again.'
            )

        return value


# V1

class UserListSerializerV1(UserListSerializer):
    pass


class UserDetailSerializerV1(UserDetailSerializer):
    pass


class UserCreateSerializerV1(UserCreateSerializer):
    pass


class UserUpdateSerializerV1(UserUpdateSerializer):
    pass


class UserPasswordChangeSerializerV1(UserPasswordChangeSerializer):
    pass
