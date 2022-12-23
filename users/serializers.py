from django.contrib.auth import get_user_model

from django_restql.mixins import DynamicFieldsMixin

from rest_framework import serializers

User = get_user_model()


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = [
            'groups',
            'user_permissions',
            'is_staff',
            'is_active',
            'is_superuser'
        ]
        read_only_fields = ['id', 'last_login']
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }


class OAuth2Serializer(serializers.Serializer):
    access_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True
    )