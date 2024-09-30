from django.db import models


class CommonModel(models.Model):
    """공통 필드를 위한 Abstract Class"""

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True
