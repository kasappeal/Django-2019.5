from rest_framework import serializers


class UserListSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class UserSerializer(UserListSerializer):

    username = serializers.CharField()
    email = serializers.EmailField()
    date_joined = serializers.DateTimeField()
    last_login = serializers.DateTimeField()
