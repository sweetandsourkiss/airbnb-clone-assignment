from re import M
from django.contrib import admin
from .models import Tweet, Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "payload",
        "user",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "user",
        "created_at",
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
