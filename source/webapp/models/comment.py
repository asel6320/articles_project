from django.contrib.auth import get_user_model
from django.db import models

from webapp.models import BaseModel


class Comment(BaseModel):
    article = models.ForeignKey('webapp.Article', related_name='comments', on_delete=models.CASCADE,
                                verbose_name='Статья')
    text = models.TextField(max_length=400, verbose_name='Комментарий')

    author = models.ForeignKey(
        get_user_model(),
        related_name="comments",
        on_delete=models.SET_DEFAULT,
        default=1
    )

    like_users = models.ManyToManyField(get_user_model(), related_name="like_comments", verbose_name="Лайки в комментариях")

    def __str__(self):
        return self.text[:20]

    class Meta:
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
