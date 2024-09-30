from django.db import models
from common.models import CommonModel  # Abstract class
from django.contrib.auth.models import User  # django 기본 제공 User


class Tweet(CommonModel):
    payload = models.CharField(
        max_length=180,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # user 삭제 시 Tweet 삭제
    )

    def __str__(self) -> str:
        return self.payload


class Like(CommonModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # user 삭제 시 Like 삭제
    )

    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,  # tweet 삭제 시 Like 삭제
    )

    def __str__(self) -> str:
        return f"{self.user.username}: [{self.tweet}]에 좋아요를 누르셨습니다."
