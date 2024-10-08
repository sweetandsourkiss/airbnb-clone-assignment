from django.db import models
from common.models import CommonModel  # Abstract class


class Tweet(CommonModel):
    payload = models.CharField(
        max_length=180,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # user 삭제 시 Tweet 삭제
        related_name="tweets",
    )

    def __str__(self) -> str:
        return self.payload

    def total_likes(self):
        return self.likes.count()


class Like(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # user 삭제 시 Like 삭제
        related_name="likes",
    )

    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,  # tweet 삭제 시 Like 삭제
        related_name="likes",
    )

    def __str__(self) -> str:
        return f"{self.user.username}: [{self.tweet}]에 좋아요를 누르셨습니다."
