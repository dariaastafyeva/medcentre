import datetime

from django.db import models
from django.utils import timezone

class Article(models.Model):
    art_title = models.CharField('название статьи', max_length = 200)
    art_text = models.TextField('содержимое статьи')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.art_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    art = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('автор коммента', max_length = 50)
    comment_text = models.CharField('текст коммента', max_length = 200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

        