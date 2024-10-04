from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # Custom Method
    def tweet(self, request, user_id):
        queryset = Tweet.objects.filter(user=user_id)
        serializer = TweetSerializer(queryset, many=True)
        return Response(serializer.data)
