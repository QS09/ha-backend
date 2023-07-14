from django.contrib.auth import get_user_model
from rest_framework import serializers


AuthUser = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = (
            'username',
            "password",
            'date_of_birth',
            'age',
            'first_name',
            'last_name',
        )

    def create(self, validated_data):
        return AuthUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = (
            'username',
            "password",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'date_of_birth',
            'age',
            'date_joined',
            'last_login',
        )


class RefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
