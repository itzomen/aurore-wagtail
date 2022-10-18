from rest_framework import serializers

from aurore.apps.users.serializers import UserSerializer


class LoginInputSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


# Output serializer with session and user data
class UserSessionOutputSerializer(serializers.Serializer):
    session = serializers.CharField()
    user = UserSerializer()


class UserTokenOutputSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserSerializer()
