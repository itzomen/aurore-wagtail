from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = (
            "id",
            "email",
            "is_admin",
            "first_name",
            "last_name",
            "last_login",
            "is_active",
        )


class UserInitSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"},
        write_only=True,
        min_length=8,
    )
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class UserFilterSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    # Important: If we use BooleanField, it will default to False
    is_admin = serializers.BooleanField(required=False)
    email = serializers.EmailField(required=False)
