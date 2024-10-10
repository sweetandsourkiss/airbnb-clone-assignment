from rest_framework.serializers import ModelSerializer
from users.models import User


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("name",)


class PublicUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "avatar",
            "name",
        )


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "id",
            "password",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions",
        )
