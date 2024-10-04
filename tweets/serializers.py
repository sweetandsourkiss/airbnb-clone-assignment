from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = "__all__"
