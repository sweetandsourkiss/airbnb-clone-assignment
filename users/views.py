from rest_framework.exceptions import ParseError, NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import PublicUserSerializer, PrivateUserSerializer
from tweets.serializers import TweetSerializer
from tweets.models import Tweet
from .models import User


class Users(APIView):
    def get(self, request):
        all_users = User.objects.all()
        serializer = PublicUserSerializer(
            all_users,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError()
        serializer = PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = PublicUserSerializer(user)
        return Response(serializer.data)
