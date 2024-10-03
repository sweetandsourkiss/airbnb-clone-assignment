from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Tweet, Like


class ElonMuskFilter(admin.SimpleListFilter):
    title = "Filter by Musk!"

    parameter_name = "has_musk"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ("True", "contains Musk"),
            ("False", "NOT contains Musk"),
        ]

    def queryset(self, request: Any, tweets: QuerySet[Any]) -> QuerySet[Any] | None:
        has_musk = self.value()
        if has_musk:
            if has_musk == "True":
                return tweets.filter(payload__contains="Elon Musk")
            else:
                return tweets.exclude(payload__contains="Elon Musk")
        else:
            return tweets


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "payload",
        "user",
        "total_likes",
        "created_at",
        "updated_at",
    )

    list_filter = (
        ElonMuskFilter,
        "user",
        "created_at",
    )

    search_fields = (
        "payload",
        "user__username",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "tweet",
        "user",
        "created_at",
    )

    list_filter = (
        "tweet",
        "user",
        "created_at",
    )

    search_fields = ("user__username",)
