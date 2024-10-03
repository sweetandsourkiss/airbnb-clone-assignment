from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from tweets.serializers import TweetSerializer
from tweets.models import Tweet
from .models import User


@api_view()
def user(request):
    return Response({"hello": True})


@api_view(["GET"])
def user_tweets(request, user_id):
    try:
        _user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise NotFound

    if request.method == "GET":
        tweets = Tweet.objects.filter(user=user_id)
        print(tweets)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
