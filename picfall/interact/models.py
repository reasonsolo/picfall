from django.db import models
from django.contrib.auth.models import User

from picfall.fall.models import Picture, Tag

from datetime import datetime

class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name = 'User',
            related_name = 'commenter')
    picture = models.ForeignKey(Picture, verbose_name = 'Picture')
    content = models.TextField('Content')
    replyto = models.ForeignKey('Comment', null = True, blank = True)

    SENTIMENT_CHOICES = (
            ('G', 'good'),
            ('B', 'bad'),
            ('N', 'neutual'),
    )
    sentiment = models.CharField('Sentiment', max_length = 1,
            choices = SENTIMENT_CHOICES, default = 'N')
    time = models.DateTimeField('Comment at', default = datetime.now())
    modifier = models.ForeignKey(User, verbose_name = 'Modifier',
            related_name = 'recommenter')
    modifiedtime = models.DateTimeField('Modified at',
            null = True, blank = True)

class Like(models.Model):
    user = models.ForeignKey(User, verbose_name = 'User')
    picture = models.ForeignKey(Picture, verbose_name = 'Picture')
    time = models.DateTimeField('Liked at', default = datetime.now())

class Repin(models.Model):
    user = models.ForeignKey(User, verbose_name = 'User')
    picture = models.ForeignKey(Picture, verbose_name = 'Picture')
    value = models.IntegerField('Value', default = 0)
    time = models.DateTimeField('Repinned at', default = datetime.now())

class AddTag(models.Model):
    user = models.ForeignKey(User, verbose_name = 'User')
    picture = models.ForeignKey(Picture, verbose_name = 'Picture')
    tag = models.ForeignKey(Tag, verbose_name = 'Tag')
    time = models.DateTimeField('Tagged at', default = datetime.now())
