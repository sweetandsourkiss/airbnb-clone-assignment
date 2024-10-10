from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import TweetSerializer, TweetDetailSerializer
from .models import Tweet


class Tweets(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(
            all_tweets,
            many=True,
        )
        print(serializer)
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            tweet = serializer.save(user=request.user)
            serializer = TweetSerializer(tweet)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class TweetDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetDetailSerializer(
            tweet,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetDetailSerializer(
            tweet,
            data=request.data,
        )
        if serializer.is_valid():
            new_tweet = serializer.save()
            serializer = TweetDetailSerializer(
                new_tweet,
                context={"request": request},
            )
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        tweet = self.get_object(pk)
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
