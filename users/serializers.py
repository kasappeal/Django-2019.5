from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class UserSerializer(UserListSerializer):

    username = serializers.CharField()
    email = serializers.EmailField()
    date_joined = serializers.ReadOnlyField()
    last_login = serializers.ReadOnlyField()


class WriteUserSerializer(UserSerializer):

    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise ValidationError('The username {0} is already used'.format(value))
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Passwords do not match')
        return attrs

    def create(self, validated_data):
        user = User()
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.username = validated_data.get('username')
        user.set_password(validated_data.get('password'))
        user.email = validated_data.get('email')
        user.save()
        return user
