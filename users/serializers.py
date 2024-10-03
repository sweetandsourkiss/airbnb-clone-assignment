from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)

    first_name = serializers.CharField(
        max_length=150,
    )
    last_name = serializers.CharField(
        max_length=150,
    )
    avatar = serializers.ImageField()
    name = serializers.CharField(
        max_length=150,
    )

    class Meta:
        model = User
        fields = "__all__"
